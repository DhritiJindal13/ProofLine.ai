from guardrail import verify_rewrite
from eval_dataset import EVAL_CASES
import time

results = []

for case in EVAL_CASES:
    verification = verify_rewrite(case["original"], case["rewrite"])

    if verification is None:
        print("Retrying after failure...")
        time.sleep(3)                                   
        verification = verify_rewrite(case["original"], case["rewrite"])

    if verification is None:
        actual_verdict = "ERROR"                      
    else:
        actual_verdict = verification.overall_verdict

    expected_verdict = case["expected_verdict"]

    results.append({
        "original": case["original"],
        "rewrite": case["rewrite"],
        "expected": expected_verdict,
        "actual": actual_verdict,
        "match": expected_verdict == actual_verdict
    })

for r in results:
    status = "MATCH" if r["match"] else "MISMATCH"
    print(f"{status:9} Expected: {r['expected']:8} Actual: {r['actual']:8} | {r['rewrite'][:60]}")

correct = sum(1 for r in results if r["match"])
print(f"\n{correct}/{len(results)} matched expected verdict")
