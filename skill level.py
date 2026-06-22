def skill_report():

    level = input("Enter level (Beginner, Intermediate, Advanced): ")

    cursor.execute("""
    SELECT e.name,
           s.skill_name
    FROM employees e
    JOIN skills s
    ON e.employee_id = s.employee_id
    WHERE s.skill_level = ?
    """, (level,))

    results = cursor.fetchall()

    print(f"\nEmployees with {level} skills:")

    for employee in results:
        print(employee)
