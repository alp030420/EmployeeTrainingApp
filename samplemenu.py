while True:

    print("\n=== Employee Skills Management System ===")
    print("1. Add Employee")
    print("2. Add Skill")
    print("3. View Records")
    print("4. Search Skill")
    print("5. Skill Level Report")
    print("6. Expiring Certifications")
    print("7. Exit")

    choice = input("Select option: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        add_skill()

    elif choice == "3":
        view_records()

    elif choice == "4":
        search_skill()

    elif choice == "5":
        skill_report()

    elif choice == "6":
        expiring_certifications()

    elif choice == "7":
        conn.close()
        break
