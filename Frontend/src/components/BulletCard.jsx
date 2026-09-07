import StatusBadge from "./StatusBadge";

const factCheckCopy = {
  PASS: "The rewrite is supported by the resume evidence.",
  REVIEW: "The claim may require confirmation before it is used.",
  FAIL: "The rewrite contains unsupported information.",
};

function renderRewriteText(text, status) {
  if (status !== "REVIEW") return text;

  return text.split(/(\b\d+(?:\.\d+)?%)/g).map((part, index) => {
    if (/^\d+(?:\.\d+)?%$/.test(part)) {
      return <mark className="review-flag" key={`${part}-${index}`}>{part}</mark>;
    }
    return part;
  });
}

function BulletCard({ item, index }) {
  const status = item.status?.toUpperCase() || "REVIEW";

  return (
    <article className={`rewrite-hunk rewrite-${status.toLowerCase()}`}>
      <header className="bullet-meta">
        <span>REWRITE {String(index + 1).padStart(2, "0")}</span>
        <span className="bullet-meta-note">VERIFIED COMPARISON</span>
      </header>

      <div className="review-grid">
        <section className="review-column original" aria-labelledby={`original-${item.id}`}>
          <span className="mini-label">ORIGINAL</span>
          <p id={`original-${item.id}`}>{item.original}</p>
        </section>

        <div className="proof-connector" aria-hidden="true"><span>→</span></div>

        <section className="review-column rewritten" aria-labelledby={`rewritten-${item.id}`}>
          <span className="mini-label">VERIFIED REWRITE</span>
          <p id={`rewritten-${item.id}`}>{renderRewriteText(item.rewritten, status)}</p>
        </section>
      </div>

      <div className="rewrite-details">
        <div className="provenance-line">
          <span className="provenance-label">FACT CHECK</span>
          <StatusBadge status={status} />
          <span className="provenance-copy">{factCheckCopy[status] || factCheckCopy.REVIEW}</span>
          <span className="provenance-divider" aria-hidden="true">·</span>
          <span className="provenance-label">SOURCE</span>
          <span className="provenance-source">{item.source?.text || "Evidence checked against the source resume."}</span>
        </div>
      </div>
    </article>
  );
}

export default BulletCard;
