const statusDescriptions = {
  PASS: "The rewrite is supported by resume evidence.",
  REVIEW: "The rewrite needs confirmation before use.",
  FAIL: "The rewrite contains unsupported information.",
};

function StatusBadge({ status }) {
  const candidate = status?.toUpperCase();
  const normalized = ["PASS", "REVIEW", "FAIL"].includes(candidate) ? candidate : "REVIEW";
  const description = statusDescriptions[normalized];

  return (
    <span
      className={`status-badge status-${normalized.toLowerCase()}`}
      title={description}
      aria-label={`Fact check ${normalized}: ${description}`}
    >
      {normalized}
    </span>
  );
}

export default StatusBadge;
