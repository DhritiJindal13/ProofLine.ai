import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


class Claim(BaseModel):
    claim: str
    status: str      
    reason: str


class VerificationResult(BaseModel):
    claims: list[Claim]
    overall_verdict: str   


def verify_rewrite(original_bullet, rewritten_bullet):
    prompt = f"""
     You are a strict fact-checker comparing an original resume bullet to a rewritten version.

    Break the REWRITTEN bullet down into individual factual claims (skills, tools,
    metrics, scope words like "scalable" or "high-traffic", responsibilities).

    For each claim, mark it as:
    - SUPPORTED: this exact claim is present in the ORIGINAL bullet
    - UNSUPPORTED: this is a specific, concrete claim NOT present in the original -
      such as a fabricated number, percentage, invented tool/technology, or an
      inflated scope/scale word (e.g. "scalable", "enterprise-grade", "high-traffic")
    - AMBIGUOUS: a general, reasonable phrase describing standard practice that is
      implied by what IS in the original, without adding any new specific fact,
      number, tool, or scale claim

    Examples to guide your judgment:
    - Original: "used JWT and RBAC" -> Rewrite says "following security best practices"
      This is AMBIGUOUS (a general phrase implied by real security practices already present),
      NOT UNSUPPORTED - it introduces no new specific fact.
    - Original: "used JWT and RBAC" -> Rewrite says "increased security by 40%"
      This is UNSUPPORTED - a specific fabricated number.
    - Original: "used JWT and RBAC" -> Rewrite says "using OAuth2 and JWT"
      This is UNSUPPORTED - a specific fabricated tool (OAuth2).

    Be strict about SPECIFIC fabricated facts (numbers, tools, named technologies,
    scale/scope adjectives) - these are always UNSUPPORTED, never AMBIGUOUS.
    Be lenient about GENERAL reasonable phrasing that adds no new specific fact.

    Original bullet:
    {original_bullet}

    Rewritten bullet:
    {rewritten_bullet}

    Then give an overall_verdict:
    - PASS: all claims are SUPPORTED
    - FAIL: at least one claim is UNSUPPORTED
    - REVIEW: only AMBIGUOUS claims exist, no UNSUPPORTED ones
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": VerificationResult,
            }
        )
        return VerificationResult.model_validate_json(response.text)
    except Exception as e:
        print("ERROR verifying rewrite:", e)
        return None



    bad_original = "Built a hotel booking website using React and Node.js."
    bad_rewrite = "Developed a scalable hotel booking platform using React and Node.js, increasing booking efficiency by 30%."

    result = verify_rewrite(bad_original, bad_rewrite)
    print("Overall verdict:", result.overall_verdict)
    for c in result.claims:
        print(f"  [{c.status}] {c.claim} -- {c.reason}")
