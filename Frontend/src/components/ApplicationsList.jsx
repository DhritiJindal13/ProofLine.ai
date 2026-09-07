function ApplicationsList({ applications = [] }) {
  return (
    <div className="applications-view">
      <header className="screen-heading applications-heading">
        <div>
          <span className="eyebrow">APPLICATIONS</span>
          <h1 id="applications-title">Saved applications.</h1>
          <p>A lightweight record of the roles you&apos;ve analyzed.</p>
        </div>
        <span className="application-count">{applications.length} TOTAL</span>
      </header>

      <div className="application-register">
        <table className="application-table">
          <caption className="sr-only">Saved resume analysis applications</caption>
          <thead>
            <tr>
              <th scope="col">COMPANY</th>
              <th scope="col">ROLE</th>
              <th scope="col">DATE</th>
              <th scope="col">MATCH</th>
            </tr>
          </thead>
          <tbody>
            {applications.map((application) => (
              <tr key={application.id}>
                <th className="application-company" scope="row">{application.company}</th>
                <td className="application-role">{application.role}</td>
                <td className="application-date">{application.date}</td>
                <td className="application-match">{application.match}%</td>
              </tr>
            ))}
            {!applications.length && (
              <tr>
                <td className="empty-applications" colSpan="4">No applications saved yet.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default ApplicationsList;
