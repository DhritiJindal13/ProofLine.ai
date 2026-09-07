const analysisSteps = [
  "Parsing resume",
  "Mapping experience",
  "Comparing skills",
  "Checking evidence",
  "Preparing rewrites",
];

function LoadingResults() {
  return (
    <div className="loading-state" aria-live="polite" aria-busy="true">
      <header className="screen-heading loading-heading">
        <div>
          <span className="eyebrow">GAP ANALYSIS</span>
          <h1 id="gap-analysis-title">Reading the evidence.</h1>
        </div>
        <p>Building a comparison from the role requirements and your resume.</p>
      </header>

      <div className="loading-progress" aria-hidden="true"><span /></div>
      <ol className="analysis-sequence">
        {analysisSteps.map((step, index) => (
          <li className={`loading-step step-${index + 1}`} key={step}>
            <span className="step-index">0{index + 1}</span>
            <span className="step-title">{step}</span>
            <span className="step-state">{index === 0 ? "ACTIVE" : "QUEUED"}</span>
          </li>
        ))}
      </ol>
      <p className="loading-message">No claims are strengthened until the source evidence is checked.</p>
    </div>
  );
}

export default LoadingResults;
