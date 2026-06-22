import sqlite3

DB_NAME = "employee_skills.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Employee table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        job_role TEXT
    )
    """)

    # Training / skills table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        skill_name TEXT,
        skill_level TEXT,
        completion_date TEXT,
        certification TEXT,
        renewal_date TEXT,
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
    """)

    conn.commit()
    conn.close()

def add_employee(employee_id, name, department, job_role):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees (employee_id, name, department, job_role)
    VALUES (?, ?, ?, ?)
    """, (employee_id, name, department, job_role))

    conn.commit()
    conn.close()

def add_training_record(employee_id, skill_name, skill_level, completion_date, certification, renewal_date):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO skills (
        employee_id, skill_name, skill_level,
        completion_date, certification, renewal_date
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (employee_id, skill_name, skill_level, completion_date, certification, renewal_date))

    conn.commit()
    conn.close()

def get_all_employees():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT employee_id, name, department, job_role
    FROM employees
    ORDER BY name
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_training_records():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT s.id,
           e.employee_id,
           e.name,
           s.skill_name,
           s.skill_level,
           s.completion_date,
           s.certification,
           s.renewal_date
    FROM skills s
    JOIN employees e ON s.employee_id = e.employee_id
    ORDER BY e.name, s.skill_name
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

def employee_exists(employee_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
    row = cursor.fetchone()

    conn.close()
    return row is not None
