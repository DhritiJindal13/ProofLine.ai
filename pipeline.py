from rewrite_engine import rewrite_bullet
from guardrail import verify_rewrite

def generate_verified_rewrite(original_bullet, jd_requirement):
    rewrite_result = rewrite_bullet(original_bullet, jd_requirement)
    if rewrite_result is None:
        return None

    rewritten = rewrite_result.rewritten_bullet
    verification = verify_rewrite(original_bullet, rewritten)

    return {
        "original": original_bullet,
        "rewritten": rewritten,
        "verdict": verification.overall_verdict,
        "claims": verification.claims,
    }


if __name__ == "__main__":
    test_cases = [
        (
            "Built a full-featured RESTful backend using Node.js, TypeScript, Express, and Prisma with SQLite.",
            "Experience building scalable backend systems"
        ),
        (
            "Implemented secure user authentication with JWT, password hashing, and Role-Based Access Control (RBAC).",
            "Strong understanding of authentication and security best practices"
        ),
        (
            "Designed a relational database system using ER diagrams, schema design, and normalization (3NF) improving query efficiency by 20%.",
            "Experience with database design and query optimization"
        ),
    ]

    for original, jd_req in test_cases:
        result = generate_verified_rewrite(original, jd_req)
        print("=" * 60)
        print("Original:", result["original"])
        print("Rewritten:", result["rewritten"])
        print("Verdict:", result["verdict"])
        for c in result["claims"]:
            print(f"  [{c.status}] {c.claim}")
        print()