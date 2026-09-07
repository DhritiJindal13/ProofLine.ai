function SkillList({ skills = [], tone = "match" }) {
  const isGap = tone === "gap";

  return (
    <ul className="skill-list" aria-label={isGap ? "Missing or unclear skills" : "Supported skills"}>
      {skills.map((skill) => (
        <li className="skill-row" key={skill.name}>
          <span className={`skill-mark ${isGap ? "gap" : "match"}`} aria-hidden="true">{isGap ? "!" : "✓"}</span>
          <div className="skill-main">
            <strong>{skill.name}</strong>
            <span>{skill.evidence}</span>
          </div>
        </li>
      ))}
      {!skills.length && <li className="empty-state">Nothing detected here.</li>}
    </ul>
  );
}

export default SkillList;
