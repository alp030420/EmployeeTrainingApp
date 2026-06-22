 cursor.execute("""
    SELECT e.name,
           s.skill_name,
           s.certification,
           s.renewal_date
    FROM employees e
    JOIN skills s
    ON e.employee_id = s.employee_id
    ORDER BY s.renewal_date
    """)

    results = cursor.fetchall()

    print("\nUpcoming Renewals")

    for row in results:
        print(row)
