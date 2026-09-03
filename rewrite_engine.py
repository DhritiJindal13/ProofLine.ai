import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


class RewriteResult(BaseModel):
    rewritten_bullet: str


def rewrite_bullet(original_bullet, jd_requirement):
    prompt = f"""
    You are helping rewrite a resume bullet point to better match a job requirement.

    STRICT RULES:
    - You may improve wording, clarity, and use JD terminology ONLY if truthful.
    - You may NOT invent metrics, numbers, percentages, tools, technologies, scale, or achievements
      that are not explicitly present in the original bullet.
    - Do not add words like "scalable", "high-traffic", "enterprise-grade" unless already stated.
    - If the original bullet has no real connection to the requirement, make only minimal
      wording improvements - do not force a connection that isn't there.

    Original resume bullet:
    {original_bullet}

    Job requirement to better align with:
    {jd_requirement}

    Rewrite the bullet following the strict rules above.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": RewriteResult,
            }
        )
        return RewriteResult.model_validate_json(response.text)
    except Exception as e:
        print("ERROR rewriting bullet:", e)
        return None

if __name__ == "__main__":
    original = "Contributed to the development of an AI-powered chatbot by implementing frontend features and integrating backend APIs to improve user interaction."
    jd_req = "Experience with AI tools like ChatGPT or GitHub Copilot"

    result = rewrite_bullet(original, jd_req)
    print("Original:", original)
    print("Rewritten:", result.rewritten_bullet)

    original2 = "Built a full-stack hotel booking platform with separate interfaces for travelers and hotel owners using React frontend and Node.js/Express backend with MongoDB."
    jd_req2 = "Experience building scalable, high-traffic web applications"

    result2 = rewrite_bullet(original2, jd_req2)
    print("\nOriginal:", original2)
    print("Rewritten:", result2.rewritten_bullet)