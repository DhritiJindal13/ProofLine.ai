from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
from sentence_transformers import SentenceTransformer, util
from datetime import date

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pdf_test import parse_resume
from jd_parser import extract_jd_requirements
from pipeline import generate_verified_rewrite
from db.database import init_db, add_application, get_all_applications

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

EXPERIENCE_DURATION_MARKERS = [
    "years of experience", "years of professional", "yrs of experience", "years in"
]


def is_experience_duration_requirement(text):
    lowered = text.lower()
    return any(marker in lowered for marker in EXPERIENCE_DURATION_MARKERS)


class HealthCheck(BaseModel):
    status: str


class ApplicationRequest(BaseModel):
    company: str
    role: str
    jd_text: str


@app.get("/health")
def health_check():
    return HealthCheck(status="ok")


@app.post("/analyze")
async def analyze(file: UploadFile, jd_text: str = Form(...)):
    temp_path = f"temp_{file.filename}"
    contents = await file.read()
    with open(temp_path, "wb") as f:
        f.write(contents)
    resume_sections = parse_resume(temp_path)
    os.remove(temp_path)

    jd_result = extract_jd_requirements(jd_text)

    resume_bullets = []
    bullet_sections = []
    for section_name, section_lines in resume_sections.items():
        if section_name == "EDUCATION":
            continue
        for line in section_lines:
            resume_bullets.append(line)
            bullet_sections.append(section_name)

    all_jd_requirements = list(dict.fromkeys(jd_result.skills + jd_result.critical_requirements))
    jd_requirements = [r for r in all_jd_requirements if not is_experience_duration_requirement(r)]
    skipped_requirements = [r for r in all_jd_requirements if is_experience_duration_requirement(r)]

    resume_embeddings = embedding_model.encode(resume_bullets)
    jd_embeddings = embedding_model.encode(jd_requirements)

    THRESHOLD = 0.35
    matches = []
    gaps = []

    for i, jd_req in enumerate(jd_requirements):
        scores = util.cos_sim(jd_embeddings[i], resume_embeddings)
        best_index = scores.argmax().item()
        best_score = scores[0][best_index].item()

        if best_score >= THRESHOLD:
            matches.append({
                "requirement": jd_req,
                "matchedBullet": resume_bullets[best_index],
                "score": round(best_score, 2),
                "section": bullet_sections[best_index],
            })
        else:
            gaps.append({
                "requirement": jd_req,
                "score": round(best_score, 2),
            })

    # dedupe by bullet text - avoid generating near-identical rewrites when
    # multiple JD requirements match the same underlying resume bullet
    seen_bullets = set()
    weak_matches = []
    for m in matches:
        if m["score"] < 0.5 and m["section"] in ("EXPERIENCE", "PROJECTS") and m["matchedBullet"] not in seen_bullets:
            weak_matches.append(m)
            seen_bullets.add(m["matchedBullet"])

    rewrites = []
    for m in weak_matches[:3]:
        result = generate_verified_rewrite(m["matchedBullet"], m["requirement"])
        if result:
            rewrites.append({
                "requirement": m["requirement"],
                "original": result["original"],
                "rewritten": result["rewritten"],
                "verdict": result["verdict"],
            })

    return {
        "resume_sections": resume_sections,
        "jd_skills": jd_result.skills,
        "jd_critical_requirements": jd_result.critical_requirements,
        "matches": matches,
        "gaps": gaps,
        "skipped_requirements": skipped_requirements,
        "rewrites": rewrites,
    }


@app.post("/applications")
def save_application(request: ApplicationRequest):
    add_application(request.company, request.role, request.jd_text, str(date.today()))
    return {"status": "saved"}


@app.get("/applications")
def list_applications():
    rows = get_all_applications()
    return [
        {"id": r[0], "company": r[1], "role": r[2], "jd_text": r[3], "date_applied": r[4]}
        for r in rows
    ]
