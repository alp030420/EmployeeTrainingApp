# Employee Skills Tracker with Skill Levels

employees = {}

def add_employee():
    name = input("Enter employee name: ")

    if name not in employees:
        employees[name] = {}
        print(f"{name} added successfully.")
    else:
        print(f"Employee '{name}' already exists.")

def add_skill():
    name = input("Enter employee name: ")

    if name in employees:
        skill = input("Enter skill name: ")

        print("\nSkill Levels:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")

        level_choice =  input("Choose skill level (1-3): ")

        levels = {
            "1": "Beginner",
            "2": "Intermediate",
            "3": "Advanced"
        }
        if level_choice in levels:
            employees[name][skill] = levels[level_choice]
            print(f"{skill}({levels[level_choice]}) added to {name}.")
        else:
            print("Invalid skill level.")
    else:
        print("Employee not found.")
    
def view_employees():
    if not employees:
        print("No employees found.")
        return

    print("\n=== Employee Skills Report ===:")

    for employee, skills in employees.items():
        print(f"\nEmployee: {employee}")

        if skills:
            for skill, level in skills.items():
                print(f"  - {skill} ({level})")
        else:
            print("  No skills added.")

def search_by_skill():
    skill = input("Enter skill to search for: ")

    found = False

    print(f"\nEmployees trained in '{skill}':")

    for employee, skills in employees.items():
        if skill in skills:
            print(f"{employee} ({skills[skill]})")
            found = True
    if not found:
        print(f"No employees found with that skill.")

def menu():
    while True:
        print("\n=== Employee Skills Tracker ===")
        print("1. Add Employee")
        print("2. Add Skill and Level")
        print("3. View All Employees")
        print("4. Search Employees by Skill")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            add_skill()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            search_by_skill()
        elif choice == "5":
            print("Exiting Employee Skills Tracker.")
            break
            print("Invalid choice. Please try again.")
    
menu()

 
