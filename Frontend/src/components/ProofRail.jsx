const steps = [
  { id: "sources", label: "Sources", shortLabel: "Sources", requiresAnalysis: false },
  { id: "gaps", label: "Gap analysis", shortLabel: "Gaps", requiresAnalysis: true },
  { id: "rewrites", label: "Verified rewrites", shortLabel: "Rewrites", requiresAnalysis: true },
  { id: "applications", label: "Applications", shortLabel: "Tracker", requiresAnalysis: false },
];

function ProofRail({ currentStep, analysisReady, onNavigate }) {
  const currentIndex = steps.findIndex((step) => step.id === currentStep);

  return (
    <nav className="proof-rail" aria-label="ProofLine workflow">
      <div className="rail-heading">
        <span>WORKFLOW</span>
        <span>Step {currentIndex + 1} of 4</span>
      </div>

      <ol className="proof-rail-list">
        {steps.map((step, index) => {
          const isCurrent = step.id === currentStep;
          const isLocked = step.requiresAnalysis && !analysisReady && !isCurrent;
          const isCompleted = analysisReady && !isCurrent && index < currentIndex && step.requiresAnalysis;
          const status = isCurrent ? "ACTIVE" : isLocked ? "LOCKED" : isCompleted ? "DONE" : "OPEN";

          return (
            <li className={`proof-rail-item ${step.id === "applications" ? "break-before" : ""}`} key={step.id}>
              <button
                type="button"
                className={`proof-rail-button ${isCurrent ? "current" : ""} ${isCompleted ? "completed" : ""}`}
                onClick={() => onNavigate(step.id)}
                disabled={isLocked}
                aria-current={isCurrent ? "step" : undefined}
                aria-label={`${step.label}, ${status.toLowerCase()}`}
              >
                <span className="proof-node" aria-hidden="true">{isCompleted ? "✓" : String(index + 1).padStart(2, "0")}</span>
                <span className="proof-label">
                  <span className="proof-label-full">{step.label}</span>
                  <span className="proof-label-short">{step.shortLabel}</span>
                </span>
                <span className="proof-status">{status}</span>
              </button>
            </li>
          );
        })}
      </ol>
    </nav>
  );
}

export default ProofRail;
