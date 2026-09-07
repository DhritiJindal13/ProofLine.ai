import SkillList from "./SkillList";
import BulletCard from "./BulletCard";
import ResumePreview from "./ResumePreview";

function getInterpretation(score) {
  if (score >= 80) return "Very strong match with limited gaps.";
  if (score >= 60) return "Strong match with a few notable gaps.";
  return "Some alignment found, with important gaps to address.";
}

function ReportHeading({ view, data, resumeFile }) {
  const isRewrites = view === "rewrites";

  return (
    <header className="screen-heading report-heading">
      <div>
        <span className="eyebrow">{isRewrites ? "VERIFIED REWRITES" : "GAP ANALYSIS"}</span>
        <h1 id={isRewrites ? "verified-rewrites-title" : "gap-analysis-title"}>
          {isRewrites ? "Stronger language, same facts." : "Gap analysis."}
        </h1>
        <p className="report-file">
          <span>FILE</span> {resumeFile?.name || "Resume"} · {data?.company || "Role"} · {data?.role || "Job description"}
        </p>
        <ResumePreview file={resumeFile} />
      </div>
      <p>
        {isRewrites
          ? "Strengthen your bullets without changing the underlying facts."
          : "Separate what the resume proves from what still needs attention."}
      </p>
    </header>
  );
}

function GapAnalysis({ data, stats, onNewAnalysis, onNext, resumeFile }) {
  return (
    <div className="report-view gap-view">
      <ReportHeading view="gaps" data={data} resumeFile={resumeFile} />

      <section className="metric-ledger" aria-labelledby="match-score-label">
        <div className="match-ledger">
          <span className="metric-label" id="match-score-label">ROLE MATCH</span>
          <div className="score-value" aria-label={`${data.matchScore} out of 100`}>
            <strong>{data.matchScore}</strong><span>%</span>
          </div>
          <p className="score-interpretation">{getInterpretation(data.matchScore)}</p>
          <div className="score-meter" role="img" aria-label={`Role match meter at ${data.matchScore} percent`}>
            <span style={{ width: `${data.matchScore}%` }} />
          </div>
          <p className="score-support">An evidence-based fit, not a prediction of hiring outcome.</p>
        </div>

        <dl className="metric-summary" aria-label="Analysis summary">
          <div><dt>MATCHES</dt><dd>{stats.matches}</dd><small>supported skills</small></div>
          <div><dt>GAPS</dt><dd>{stats.gaps}</dd><small>missing or unclear</small></div>
          <div><dt>REWRITES</dt><dd>{stats.rewrites}</dd><small>bullets reviewed</small></div>
        </dl>
      </section>

      <section className="evidence-section" aria-labelledby="evidence-title">
        <div className="section-heading compact-heading">
          <div>
            <span className="eyebrow">EVIDENCE MAP</span>
            <h2 id="evidence-title">What the resume supports.</h2>
          </div>
        </div>

        <div className="evidence-columns">
          <section className="evidence-column missing-column" aria-labelledby="missing-title">
            <div className="column-head">
              <div><span className="column-label">MISSING / UNCLEAR</span><h3 id="missing-title">Gaps to address</h3></div>
              <span className="column-count">{String(stats.gaps).padStart(2, "0")} ITEMS</span>
            </div>
            <SkillList skills={data.missingSkills} tone="gap" />
          </section>

          <section className="evidence-column supported-column" aria-labelledby="supported-title">
            <div className="column-head">
              <div><span className="column-label">SUPPORTED</span><h3 id="supported-title">Evidence found</h3></div>
              <span className="column-count">{String(stats.matches).padStart(2, "0")} SKILLS</span>
            </div>
            <SkillList skills={data.matchedSkills} />
          </section>
        </div>
      </section>

      <div className="screen-actions">
        <button className="secondary-button" type="button" onClick={onNewAnalysis}>New analysis</button>
        <button className="primary-button" type="button" onClick={onNext}>Review rewrites <span aria-hidden="true">→</span></button>
      </div>
    </div>
  );
}

function VerifiedRewrites({ data, onNewAnalysis, onBack, isSaved, resumeFile, companyName, roleName, onCompanyChange, onRoleChange, onSaveApplication }) {
  return (
    <div className="report-view rewrites-view">
      <ReportHeading view="rewrites" data={data} resumeFile={resumeFile} />

      <aside className="guardrail-note" role="note">
        <span className="guardrail-mark" aria-hidden="true">✓</span>
        <div>
          <span className="guardrail-label">FACT-CHECKED BY DESIGN</span>
          <p>Suggestions are constrained by evidence in your resume. Unsupported metrics or responsibilities are flagged for review.</p>
        </div>
      </aside>

      <div className="rewrite-list" aria-label="Verified resume rewrites">
        {data.rewrites?.map((item, index) => (
          <BulletCard key={item.id || index} item={item} index={index} />
        ))}
      </div>

      <section className="save-application-form" aria-label="Save this application">
        <input
          type="text"
          placeholder="Company name"
          value={companyName}
          onChange={(e) => onCompanyChange(e.target.value)}
        />
        <input
          type="text"
          placeholder="Role"
          value={roleName}
          onChange={(e) => onRoleChange(e.target.value)}
        />
      </section>

      <div className="screen-actions rewrites-actions">
        <button className="text-button" type="button" onClick={onBack}>← Back to gap analysis</button>
        <div className="action-group">
          <button className="secondary-button" type="button" onClick={onNewAnalysis}>New analysis</button>
          <button className="primary-button" type="button" onClick={onSaveApplication} disabled={isSaved}>
            {isSaved ? "Saved" : "Save application"}
          </button>
        </div>
      </div>
    </div>
  );
}

function ResultsView({ view = "gaps", data, resumeFile, stats, onNewAnalysis, onNext, onBack, isSaved = false, companyName, roleName, onCompanyChange, onRoleChange, onSaveApplication }) {
  if (!data) return null;

  return view === "rewrites" ? (
    <VerifiedRewrites
      data={data}
      resumeFile={resumeFile}
      onNewAnalysis={onNewAnalysis}
      onBack={onBack}
      isSaved={isSaved}
      companyName={companyName}
      roleName={roleName}
      onCompanyChange={onCompanyChange}
      onRoleChange={onRoleChange}
      onSaveApplication={onSaveApplication}
    />
  ) : (
    <GapAnalysis
      data={data}
      resumeFile={resumeFile}
      stats={stats}
      onNewAnalysis={onNewAnalysis}
      onNext={onNext}
    />
  );
}

export default ResultsView;
