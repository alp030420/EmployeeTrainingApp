import sqlite3

DB_NAME = "employee_skills.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table 
    pass

conn = sqlite3.connect("smployee_skills.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    skill_name TEXT,
    SKILL_LEVEL TEXT,
    completion_date TEXT,
    certification TEXT,
    renewal_date TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
)
""")

conn.commit()