import sqlite3


def init_db():
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            role TEXT,
            jd_text TEXT,
            date_applied TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_application(company, role, jd_text, date_applied):
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO applications (company, role, jd_text, date_applied) VALUES (?, ?, ?, ?)",
        (company, role, jd_text, date_applied)
    )
    conn.commit()
    conn.close()


def get_all_applications():
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows