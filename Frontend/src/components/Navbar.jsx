function Navbar({ darkMode, onToggleTheme, onNavigate }) {
  return (
    <header className="site-header">
      <div className="page-container nav-inner">
        <button className="brand" type="button" onClick={onNavigate} aria-label="ProofLine home">
          <span className="brand-mark">P</span>
          <span>ProofLine</span>
        </button>

        <button
          className="theme-toggle"
          type="button"
          onClick={onToggleTheme}
          aria-label={darkMode ? "Switch to light mode" : "Switch to dark mode"}
          aria-pressed={darkMode}
          title={darkMode ? "Switch to light mode" : "Switch to dark mode"}
        >
          <span className="theme-glyph" aria-hidden="true">{darkMode ? "☀" : "☾"}</span>
        </button>
      </div>
    </header>
  );
}

export default Navbar;
