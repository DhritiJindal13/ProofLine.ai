import { useEffect, useMemo, useState } from "react";
import Navbar from "./components/Navbar";
import ProofRail from "./components/ProofRail";
import Hero from "./components/Hero";
import UploadForm from "./components/UploadForm";
import ResultsView from "./components/ResultsView";
import ApplicationsList from "./components/ApplicationsList";
import LoadingResults from "./components/LoadingResults";

const analysisSteps = new Set(["gaps", "rewrites"]);

function App() {
  const [currentStep, setCurrentStep] = useState("sources");
  const [analysisState, setAnalysisState] = useState("idle");
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [results, setResults] = useState(null);
  const [applications, setApplications] = useState([]);
  const [darkMode, setDarkMode] = useState(false);
  const [isCurrentApplicationSaved, setIsCurrentApplicationSaved] = useState(false);
  const [companyName, setCompanyName] = useState("");
  const [roleName, setRoleName] = useState("");

  useEffect(() => {
    document.documentElement.dataset.theme = darkMode ? "dark" : "light";
  }, [darkMode]);

  const analysisReady = Boolean(results && analysisState === "complete");

  const handleNavigate = (step) => {
    if (analysisSteps.has(step) && !analysisReady && step !== currentStep) return;
    setCurrentStep(step);
  };

  const handleAnalyze = async ({ file, jobDescription: jd }) => {
    setResumeFile(file);
    setJobDescription(jd);
    setAnalysisState("loading");
    setIsCurrentApplicationSaved(false);
    setCurrentStep("gaps");

    try {
      const formData = new FormData();
      formData.append("file", file);
      formData.append("jd_text", jd);

      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Analysis failed");

      const data = await response.json();

      const matchedSkills = data.matches.map((m) => ({
        name: m.requirement,
        evidence: m.matchedBullet + " (score: " + m.score + ")",
      }));

      const missingSkills = data.gaps.map((g) => ({
        name: g.requirement,
        evidence: "No strong match found (score: " + g.score + ")",
      }));

      const rewrites = data.rewrites.map((r) => ({
        requirement: r.requirement,
        original: r.original,
        rewritten: r.rewritten,
        verdict: r.verdict,
      }));

      const totalConsidered = matchedSkills.length + missingSkills.length;
      const matchScore = totalConsidered > 0
        ? Math.round((matchedSkills.length / totalConsidered) * 100)
        : 0;

      setResults({
        matchedSkills,
        missingSkills,
        rewrites,
        matchScore,
        resumeSections: data.resume_sections,
        skippedRequirements: data.skipped_requirements,
      });
      setAnalysisState("complete");
    } catch (error) {
      console.error("Analysis error:", error);
      setAnalysisState("error");
    }
  };

  const handleSaveApplication = () => {
    if (isCurrentApplicationSaved) return;
    if (!companyName.trim() || !roleName.trim()) {
      alert("Please enter both a company name and a role before saving.");
      return;
    }

    const next = {
      id: Date.now(),
      company: companyName.trim(),
      role: roleName.trim(),
      date: new Intl.DateTimeFormat("en-GB", {
        day: "2-digit",
        month: "short",
        year: "numeric",
      }).format(new Date()),
      match: results && results.matchScore ? results.matchScore : 0,
    };
    setApplications(function (current) { return [next].concat(current); });
    setIsCurrentApplicationSaved(true);
  };

  const handleReset = () => {
    setCurrentStep("sources");
    setAnalysisState("idle");
    setResumeFile(null);
    setJobDescription("");
    setResults(null);
    setIsCurrentApplicationSaved(false);
    setCompanyName("");
    setRoleName("");
  };

  const stats = useMemo(function () {
    return {
      matches: results && results.matchedSkills ? results.matchedSkills.length : 0,
      gaps: results && results.missingSkills ? results.missingSkills.length : 0,
      rewrites: results && results.rewrites ? results.rewrites.length : 0,
    };
  }, [results]);

  const renderStep = () => {
    if (currentStep === "sources") {
      return (
        <section className="step-screen sources-screen" aria-labelledby="sources-title">
          <Hero />
          <UploadForm
            onAnalyze={handleAnalyze}
            resumeFile={resumeFile}
            jobDescription={jobDescription}
          />
        </section>
      );
    }

    if (currentStep === "gaps") {
      return (
        <section className="step-screen analysis-screen" aria-labelledby="gap-analysis-title" aria-live="polite" aria-busy={analysisState === "loading"}>
          {analysisState === "loading" ? (
            <LoadingResults />
          ) : (
            <ResultsView
              view="gaps"
              data={results}
              resumeFile={resumeFile}
              stats={stats}
              onNewAnalysis={handleReset}
              onNext={() => setCurrentStep("rewrites")}
            />
          )}
        </section>
      );
    }

    if (currentStep === "rewrites") {
      return (
        <section className="step-screen rewrites-screen" aria-labelledby="verified-rewrites-title">
          <ResultsView
            view="rewrites"
            data={results}
            resumeFile={resumeFile}
            stats={stats}
            onNewAnalysis={handleReset}
            onBack={() => setCurrentStep("gaps")}
            isSaved={isCurrentApplicationSaved}
            companyName={companyName}
            roleName={roleName}
            onCompanyChange={setCompanyName}
            onRoleChange={setRoleName}
            onSaveApplication={handleSaveApplication}
          />
        </section>
      );
    }

    return (
      <section className="step-screen applications-screen" aria-labelledby="applications-title">
        <ApplicationsList applications={applications} />
      </section>
    );
  };

  return (
    <div className="app-shell">
      <Navbar
        darkMode={darkMode}
        onToggleTheme={() => setDarkMode((value) => !value)}
        onNavigate={() => handleNavigate("sources")}
      />

      <main className="app-main">
        <div className="page-container workspace-layout">
          <ProofRail
            currentStep={currentStep}
            analysisReady={analysisReady}
            onNavigate={handleNavigate}
          />
          <div className="screen-content">{renderStep()}</div>
        </div>
      </main>

      <footer className="site-footer">
        <div className="page-container footer-inner">
          <div className="footer-brand">
            <span className="brand-mark">P</span>
            <span>ProofLine</span>
          </div>
          <div className="footer-right">
            <span>Evidence over exaggeration.</span>
            <span>v0.1</span>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
