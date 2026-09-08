ProofLine

An AI resume-to-job matching tool that finds real gaps between a resume and a job description, rewrites weak bullet points to close those gaps, and then independently fact-checks every rewrite before showing it to the user.

Most AI resume tools will happily turn "Built a hotel booking website using React and Node.js" into "Developed a scalable hotel booking platform serving 50,000 users, increasing bookings by 30%." Neither number in that sentence exists anywhere in the original. ProofLine is built specifically to prevent that: a second, independent model checks every rewrite against the source resume before it's ever shown, claim by claim.

1. What it actually does
Parses an uploaded resume (PDF or DOCX) into structured sections.
Extracts structured requirements from a pasted job description (skills, responsibilities, must-haves vs. nice-to-haves).
Matches the two using a combination of exact keyword overlap and semantic (embedding-based) similarity, so a resume that says "React" still gets credit against a JD asking for "frontend JavaScript frameworks."
Flags genuine gaps and produces a transparent match score.
For weak (but present) matches, generates a rewritten bullet aligned to the JD's language.
Runs every rewrite through a separate verification pass that checks each individual claim against the original text and labels it supported, unsupported, or ambiguous.
Lets the user track which resume version was used for which application.
2. Why the guardrail exists

An LLM asked to "rewrite this bullet to sound stronger" has no built-in incentive to stay factual. It will reach for a plausible-sounding metric because that's what a strong bullet point usually looks like in its training data, not because that metric is true.

ProofLine treats the rewrite step and the verification step as two separate jobs, run by two independent model calls:

The rewriter is constrained by explicit rules: no invented numbers, no invented tools, no invented scale ("scalable," "enterprise-grade," etc.) unless the original text already says so.
The verifier receives only the original bullet and the candidate rewrite, decomposes the rewrite into individual factual claims, and checks each one against the source.

A single model checking its own output has no reason to catch its own mistake — it already "believes" what it just wrote. A second, separate pass is structurally better positioned to catch fabrication, because it isn't the one that generated the claim in the first place.

3. Evaluation, with real numbers

Claiming a guardrail works and measuring whether it works are different things. This one was tested against a 34-case dataset built by hand, covering honest rewrites, fabricated metrics, fabricated tools, exaggerated scope, fabricated responsibilities, and deliberately ambiguous edge cases.

Results on the core safety-relevant distinction (does a rewrite contain a fabrication or not):

Metric	Result
Precision	100% — every rewrite flagged as a failure was a genuine fabrication
Recall	100% — every genuine fabrication was caught

The one place the system did not perform well on the first pass: an intermediate "needs review" category, meant for genuinely ambiguous rewrites, was barely used — the guardrail defaulted to a hard rejection on almost every borderline case instead of flagging it for human review. The cause was a prompt instruction ("be strict") that was overpowering the model's willingness to use the softer category. Adding contrasting examples to the prompt fixed it, verified on the cases that had failed originally.

That failure and fix are documented here on purpose. A system that only reports a clean first-try result usually means the evaluation wasn't looked at closely enough.

4. Architecture
React frontend
      |
      v
FastAPI backend
      |
      +-- Resume parser        (pdfplumber / python-docx)
      +-- JD parser            (Gemini, structured JSON output)
      +-- Matching engine      (keyword overlap + sentence embeddings)
      +-- Rewrite engine       (Gemini, constrained prompt)
      +-- Verification engine  (Gemini, independent claim-checking pass)
      |
      v
SQLite (application history)

The project started as a Streamlit prototype to prove the pipeline worked before being rebuilt with a proper frontend/backend split.

5. Stack
Frontend: React (Vite), plain CSS, no component library
Backend: FastAPI
LLM: Google Gemini, structured output enforced via Pydantic schemas
Semantic matching: sentence-transformers, run locally
Storage: SQLite
Parsing: pdfplumber, python-docx
Deliberately not used
RAG — there's no large external corpus to retrieve from. A resume and a JD are both small enough to hand directly to the model.
LangChain or a vector database — the pipeline is five sequential calls. A framework adds a layer of abstraction with nothing to abstract; direct API calls are easier to reason about and easier to explain.
Fine-tuning — there's no training data need here that prompting a general-purpose model doesn't already solve.
Docker — not required for the current setup; would matter if this were deployed to a raw VM needing an environment guarantee.
6. What doesn't work yet, on purpose or otherwise
Embedding similarity is a relative signal, not proof of a match. The matching threshold was set by inspecting real output, not derived from a formula, and it occasionally lets a loose match through on compound requirements like "Python, JavaScript, or a similar language."
No OCR. Scanned or image-based resumes aren't supported — only resumes with a real text layer. This was a deliberate scope cut, not an oversight; OCR is a separate problem from matching and verification.
No full-resume regeneration. The tool surfaces gap analysis and verified bullet rewrites; a person still decides what actually goes into their resume. That's intentional — a tool that silently rewrites your whole resume removes the one place a human should stay in the loop.
The backend currently runs locally rather than on a hosted platform. The embedding step needs more memory than free-tier hosting typically allows; running it locally was the more honest trade-off given the constraints of this project, rather than switching the embedding approach purely to force a live demo.
7. Running it locally

Backend

cd backend
pip install -r ../requirements.txt
uvicorn main:app --reload

Frontend

cd Frontend
npm install
npm run dev

Requires a GEMINI_API_KEY, set in a .env file at the project root. See .env.example for the expected format.

8. If this were going further
Move the matching threshold from a fixed value to something calibrated against a larger labeled dataset.
Add a baseline comparison — same rewrites, with the guardrail turned off — to quantify exactly how much the verification step changes outcomes, not just whether it exists.
Expand the evaluation set well past 34 cases for a statistically sturdier precision/recall figure.
Host the backend somewhere with enough memory to run the embedding model without local-only compromises. 
