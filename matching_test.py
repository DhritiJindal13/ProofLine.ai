from pdf_test import parse_resume
from jd_parser import extract_jd_requirements
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

resume_sections = parse_resume("resume.pdf")

resume_bullets =[]
for section_lines in  resume_sections.values():
    resume_bullets.extend(section_lines)

real_jd ="""
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

jd_result = extract_jd_requirements(real_jd)
jd_requirements = jd_result.skills + jd_result.critical_requirements

resume_embeddings = model.encode(resume_bullets)
jd_embeddings = model.encode(jd_requirements)

for i, jd_req in enumerate(jd_requirements):
    print(f"\nJD Requirement: {jd_req}")
    scores = util.cos_sim(jd_embeddings[i], resume_embeddings)  
    best_index = scores.argmax().item()                          
    print(f"  Best match ({scores[0][best_index]:.2f}): {resume_bullets[best_index]}")