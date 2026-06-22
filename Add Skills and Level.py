# View All Employees and Skills
def view_records():
   
    cursor.execute("""
    SELECT e.employee_id,
        e.name,
        s.skill_name,
        s.skill_level,
        s.completion_date,
        s.certification,
        s.renewal_date
    FROM employees e
    LEFT JOIN skills s
    ON e.employee_id = s.employee_id
    """)

    records = cursor.fetchall()

    for record in records:
        print(f"Employee ID: {record[0]}, Name: {record[1]}, Skill: {record[2]}, Completion Date: {record[3]}, Certification Date: {record[4]}, Renewal Date: {record[5]}")


