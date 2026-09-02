import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


# --- schema defining the exact shape we want Gemini's answer in ---
class JDRequirements(BaseModel):
    skills: list[str]
    responsibilities: list[str]
    critical_requirements: list[str]
    nice_to_have: list[str]


def extract_jd_requirements(jd_text):
    prompt = f"""
    Extract structured requirements from this job description.
    Categorize skills, responsibilities, critical (must-have) requirements,
    and nice-to-have requirements.

    Job description:
    {jd_text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": JDRequirements,
            }
        )
        return JDRequirements.model_validate_json(response.text)
    except Exception as e:
        print("ERROR extracting JD requirements:", e)
        return None


# --- quick test on a real JD ---
real_jd = """
QA Intern
Job Title: QA Intern
Location: Gurugram (WFO)
Experience: Freshers / Final Year Students
Internship Duration: 3–6 Months
Job Summary
We are looking for a motivated and detail-oriented QA Intern to join our Quality Assurance team. This
internship is an excellent opportunity for fresh graduates or final-year students who are passionate about
software testing and want to gain hands-on experience in testing web applications.
The ideal candidate should have a basic understanding of software testing concepts, SDLC, STLC, and test
case design. Good knowledge of Object-Oriented Programming (OOPs) concepts is required, along with basic
knowledge of AI tools. Knowledge of Java will be an added advantage.
Key Responsibilities
•
Understand business requirements and functional specifications.
•
Design and execute manual test cases based on requirements.
•
Identify, document, and report software defects.
•
Perform functional, regression, and smoke testing.
•
Validate bug fixes and perform re-testing.
•
Maintain test cases and testing documentation.
•
Participate in daily stand-ups and QA team discussions.
•
Collaborate with developers and senior QA engineers to ensure product quality.
•
Learn automation testing concepts and industry best practices.
Required Skills
Software Testing
•
Basic understanding of Software Development Life Cycle (SDLC).
•
Basic understanding of Software Testing Life Cycle (STLC).
•
Knowledge of different testing types:
◦
Functional Testing
◦
Regression Testing
◦
Smoke Testing
◦
Sanity Testing
◦
Retesting
•
Basic understanding of Bug Life Cycle.
•
Ability to write simple and effective test cases.
Programming
•
Good understanding of Object-Oriented Programming (OOPs) concepts.
•
Basic knowledge of Java (added advantage).
AI Knowledge
•
Basic knowledge of AI tools (e.g., ChatGPT, GitHub Copilot).
"""

result = extract_jd_requirements(real_jd)
print(result)