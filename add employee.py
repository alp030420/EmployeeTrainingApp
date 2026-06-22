# Add employee
def add_employee():
    employee_id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    
    cursor.execute(
        "INSERT INTO employees (employee_id, name) VALUES (?, ?)",
        (employee_id, name)
    )

    conn.commit()
    print("Employee added successfully.")
        
