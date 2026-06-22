def add_skill():
    employee_id = int(input("Employee ID: "))
    skill_name = input("Skill Name: ")
    skill_level = input("Level (Beginner, Intermediate, Advanced): ")
    completion_date = input("Completion Date (YYYY-MM-DD): ")
    certification = input("Certification Name: ")
    renewal_date = input("Renewal Date (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO skills (employee_id, skill_name, skill_level, completion_date, certification, renewal_date) VALUES (?, ?, ?, ?, ?, ?)",
        (employee_id, skill_name, skill_level, completion_date, certification, renewal_date)
    )   VALUES (?, ?, ?, ?, ?, ?)
    """,
        (employee_id,
        skill_name,
        skill_level, 
        completion_date,
        certification,
        renewal_date)
    ))
   
    conn.committ()
    print("Skill record added successfully.")
