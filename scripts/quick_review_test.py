from guardrail import verify_rewrite
import time

case2_original = "Implemented IP-based rate limiting middleware to prevent API abuse (100 requests/minute per client)."
case2_rewrite = "Implemented security middleware to prevent API abuse, including rate limiting best practices."

result = None
attempts = 0
while result is None and attempts < 3:
    result = verify_rewrite(case2_original, case2_rewrite)
    attempts += 1
    if result is None and attempts < 3:
        print("Retrying...")
        time.sleep(15)

if result:
    print("Verdict:", result.overall_verdict)
    for c in result.claims:
        print(f"  [{c.status}] {c.claim}")
else:
    print("Failed after retries.")