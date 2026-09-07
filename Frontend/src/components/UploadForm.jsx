import { useEffect, useRef, useState } from "react";

const MAX_FILE_SIZE = 10 * 1024 * 1024;
const MIN_JOB_DESCRIPTION_LENGTH = 30;

function UploadForm({ onAnalyze, resumeFile, jobDescription }) {
  const inputRef = useRef(null);
  const [dragActive, setDragActive] = useState(false);
  const [localFile, setLocalFile] = useState(resumeFile);
  const [localJD, setLocalJD] = useState(jobDescription || "");
  const [fileError, setFileError] = useState("");

  useEffect(() => {
    setLocalFile(resumeFile);
    setLocalJD(jobDescription || "");
    setFileError("");
  }, [resumeFile, jobDescription]);

  const setFile = (file) => {
    if (!file) return;

    const isPdf = file.type === "application/pdf" || file.name.toLowerCase().endsWith(".pdf");
    if (!isPdf) {
      setFileError("Please choose a PDF resume.");
      return;
    }

    if (file.size === 0) {
      setFileError("This file is empty. Choose a readable PDF resume.");
      return;
    }

    if (file.size > MAX_FILE_SIZE) {
      setFileError("This file is larger than 10 MB. Choose a smaller PDF resume.");
      return;
    }

    setLocalFile(file);
    setFileError("");
  };

  const clearFile = () => {
    setLocalFile(null);
    setFileError("");
    if (inputRef.current) inputRef.current.value = "";
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setDragActive(false);
    setFile(event.dataTransfer.files?.[0]);
  };

  const canAnalyze = Boolean(localFile && localJD.trim().length >= MIN_JOB_DESCRIPTION_LENGTH);
  const descriptionIsShort = localJD.trim().length > 0 && localJD.trim().length < MIN_JOB_DESCRIPTION_LENGTH;

  const submit = (event) => {
    event.preventDefault();
    if (!canAnalyze) return;
    onAnalyze({ file: localFile, jobDescription: localJD.trim() });
  };

  return (
    <form className="source-worksheet" onSubmit={submit} noValidate>
      <div className="input-grid">
        <section className="input-panel" aria-labelledby="resume-panel-title">
          <div className="panel-head">
            <div className="panel-title">
              <span className="panel-index">01</span>
              <h2 id="resume-panel-title">RESUME</h2>
            </div>
            <span className="file-rule">PDF ONLY</span>
          </div>

          <input
            ref={inputRef}
            id="resume-file"
            type="file"
            accept=".pdf,application/pdf"
            hidden
            onChange={(event) => setFile(event.target.files?.[0])}
            aria-describedby="resume-help resume-error"
          />

          {!localFile ? (
            <button
              type="button"
              className={`dropzone ${dragActive ? "drag-active" : ""}`}
              onClick={() => inputRef.current?.click()}
              onDragOver={(event) => { event.preventDefault(); setDragActive(true); }}
              onDragLeave={() => setDragActive(false)}
              onDrop={handleDrop}
              aria-controls="resume-file"
              aria-describedby="resume-help resume-error"
            >
              <span className="upload-symbol" aria-hidden="true">↑</span>
              <strong>DROP YOUR RESUME HERE</strong>
              <span>PDF up to 10 MB · click to browse</span>
            </button>
          ) : (
            <div className="file-selected" role="status" aria-live="polite">
              <div className="pdf-icon" aria-hidden="true">PDF</div>
              <div className="file-copy">
                <strong>{localFile.name}</strong>
                <span>{(localFile.size / 1024 / 1024).toFixed(2)} MB · ready to analyze</span>
              </div>
              <div className="file-actions">
                <button type="button" className="file-action" onClick={() => inputRef.current?.click()}>Replace</button>
                <button type="button" className="file-remove" onClick={clearFile}>Remove</button>
              </div>
            </div>
          )}

          <div className="panel-foot" id="resume-help">
            <span>Used only for this analysis.</span>
            <span>MAX 10 MB</span>
          </div>
          {fileError && <p className="field-error" id="resume-error" role="alert">{fileError}</p>}
        </section>

        <section className="input-panel" aria-labelledby="jd-panel-title">
          <div className="panel-head">
            <div className="panel-title">
              <span className="panel-index">02</span>
              <h2 id="jd-panel-title">JOB DESCRIPTION</h2>
            </div>
            <span className="file-rule">{localJD.length} CHARS</span>
          </div>

          <label className="sr-only" htmlFor="job-description">Job description</label>
          <textarea
            id="job-description"
            className="jd-input"
            value={localJD}
            onChange={(event) => setLocalJD(event.target.value)}
            placeholder="Paste the job description here..."
            aria-describedby="jd-help jd-error"
          />

          <div className="panel-foot" id="jd-help">
            <span>Include responsibilities and requirements.</span>
            <span>MIN 30 CHARS</span>
          </div>
          {descriptionIsShort && (
            <p className="field-error" id="jd-error" role="status">
              Add {MIN_JOB_DESCRIPTION_LENGTH - localJD.trim().length} more characters to continue.
            </p>
          )}
        </section>
      </div>

      <div className="analyze-bar">
        <div className="readiness" aria-live="polite">
          <span className={localFile ? "ready" : ""}><i aria-hidden="true" /> Resume {localFile ? "ready" : "required"}</span>
          <span className={localJD.trim().length >= MIN_JOB_DESCRIPTION_LENGTH ? "ready" : ""}>
            <i aria-hidden="true" /> Job description {localJD.trim().length >= MIN_JOB_DESCRIPTION_LENGTH ? "ready" : "required"}
          </span>
          <span className="form-status">{canAnalyze ? "Ready to compare" : "Add a PDF and 30+ characters to continue."}</span>
        </div>
        <button className="primary-button analyze-button" type="submit" disabled={!canAnalyze}>
          Analyze match <span aria-hidden="true">→</span>
        </button>
      </div>
    </form>
  );
}

export default UploadForm;
