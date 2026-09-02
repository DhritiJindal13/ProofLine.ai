import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


class Claim(BaseModel):
    claim: str
    status: str        # "SUPPORTED", "UNSUPPORTED", or "AMBIGUOUS"
    reason: str


class VerificationResult(BaseModel):
    claims: list[Claim]
    overall_verdict: str    # "PASS", "FAIL", or "REVIEW"


def verify_rewrite(original_bullet, rewritten_bullet):
    prompt = f"""
    You are a strict fact-checker comparing an original resume bullet to a rewritten version.

    Break the REWRITTEN bullet down into individual factual claims (skills, tools,
    metrics, scope words like "scalable" or "high-traffic", responsibilities).

    For each claim, mark it as:
    - SUPPORTED: this exact claim is present in the ORIGINAL bullet
    - UNSUPPORTED: this claim is NOT present in the original - it was invented or exaggerated
    - AMBIGUOUS: implied but not explicitly stated in the original

    Be strict: any specific number, percentage, or scale/scope word ("scalable",
    "high-traffic", "enterprise-grade") that is not explicitly in the original
    must be marked UNSUPPORTED.

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
            model="gemini-3.6-flash",
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


#if __name__ == "__main__":
    bad_original = "Built a hotel booking website using React and Node.js."
    bad_rewrite = "Developed a scalable hotel booking platform using React and Node.js, increasing booking efficiency by 30%."

    result = verify_rewrite(bad_original, bad_rewrite)
    print("Overall verdict:", result.overall_verdict)
    for c in result.claims:
        print(f"  [{c.status}] {c.claim} -- {c.reason}")