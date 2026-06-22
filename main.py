import tkinter as tk
from tkinter import ttk, messagebox
from database import (
    create_tables,
    add_employee,
    add_training_record,
    get_all_employees,
    get_all_training_records,
    employee_exists
)

# ----------------------------
# Set up database
# ----------------------------
create_tables()

# ----------------------------
# Functions
# ----------------------------
def save_employee():
    emp_id = emp_id_entry.get().strip()
    name = name_entry.get().strip()
    department = dept_entry.get().strip()
    job_role = role_entry.get().strip()

    if not emp_id or not name:
        messagebox.showerror("Error", "Employee ID and Name are required.")
        return

    try:
        emp_id = int(emp_id)
        add_employee(emp_id, name, department, job_role)
        messagebox.showinfo("Success", "Employee added successfully.")

        emp_id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        dept_entry.delete(0, tk.END)
        role_entry.delete(0, tk.END)

        load_employees()

    except ValueError:
        messagebox.showerror("Error", "Employee ID must be a number.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def save_training():
    emp_id = training_emp_id_entry.get().strip()
    skill_name = skill_entry.get().strip()
    skill_level = skill_level_combo.get().strip()
    completion_date = completion_entry.get().strip()
    certification = cert_entry.get().strip()
    renewal_date = renewal_entry.get().strip()

    if not emp_id or not skill_name:
        messagebox.showerror("Error", "Employee ID and Skill Name are required.")
        return

    try:
        emp_id = int(emp_id)

        if not employee_exists(emp_id):
            messagebox.showerror("Error", "Employee ID does not exist. Add employee first.")
            return

        add_training_record(
            emp_id,
            skill_name,
            skill_level,
            completion_date,
            certification,
            renewal_date
        )

        messagebox.showinfo("Success", "Training record added successfully.")

        training_emp_id_entry.delete(0, tk.END)
        skill_entry.delete(0, tk.END)
        skill_level_combo.set("")
        completion_entry.delete(0, tk.END)
        cert_entry.delete(0, tk.END)
        renewal_entry.delete(0, tk.END)

        load_training_records()

    except ValueError:
        messagebox.showerror("Error", "Employee ID must be a number.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def load_employees():
    for row in employee_tree.get_children():
        employee_tree.delete(row)

    employees = get_all_employees()
    for employee in employees:
        employee_tree.insert("", tk.END, values=employee)


def load_training_records():
    for row in training_tree.get_children():
        training_tree.delete(row)

    records = get_all_training_records()
    for record in records:
        training_tree.insert("", tk.END, values=record)


# ----------------------------
# Main Window
# ----------------------------
root = tk.Tk()
root.title("Employee Skills Management System")
root.geometry("1200x750")
root.configure(bg="#f4f6f8")

title_label = tk.Label(
    root,
    text="Employee Skills Management System",
    font=("Arial", 22, "bold"),
    bg="#f4f6f8",
    fg="#1f2937"
)
title_label.pack(pady=15)

# ----------------------------
# Employee Form Frame
# ----------------------------
employee_frame = tk.LabelFrame(
    root,
    text="Add Employee",
    font=("Arial", 12, "bold"),
    bg="white",
    padx=15,
    pady=15
)
employee_frame.pack(fill="x", padx=20, pady=10)

tk.Label(employee_frame, text="Employee ID:", bg="white", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
emp_id_entry = tk.Entry(employee_frame, width=25)
emp_id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(employee_frame, text="Employee Name:", bg="white", font=("Arial", 11)).grid(row=0, column=2, sticky="w", pady=5)
name_entry = tk.Entry(employee_frame, width=25)
name_entry.grid(row=0, column=3, padx=10, pady=5)

tk.Label(employee_frame, text="Department:", bg="white", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
dept_entry = tk.Entry(employee_frame, width=25)
dept_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(employee_frame, text="Job Role:", bg="white", font=("Arial", 11)).grid(row=1, column=2, sticky="w", pady=5)
role_entry = tk.Entry(employee_frame, width=25)
role_entry.grid(row=1, column=3, padx=10, pady=5)

tk.Button(
    employee_frame,
    text="Add Employee",
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    width=18,
    command=save_employee
).grid(row=2, column=0, columnspan=4, pady=15)

# ----------------------------
# Training Form Frame
# ----------------------------
training_frame = tk.LabelFrame(
    root,
    text="Add Training Record",
    font=("Arial", 12, "bold"),
    bg="white",
    padx=15,
    pady=15
)
training_frame.pack(fill="x", padx=20, pady=10)

tk.Label(training_frame, text="Employee ID:", bg="white", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
training_emp_id_entry = tk.Entry(training_frame, width=25)
training_emp_id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(training_frame, text="Skill Name:", bg="white", font=("Arial", 11)).grid(row=0, column=2, sticky="w", pady=5)
skill_entry = tk.Entry(training_frame, width=25)
skill_entry.grid(row=0, column=3, padx=10, pady=5)

tk.Label(training_frame, text="Skill Level:", bg="white", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
skill_level_combo = ttk.Combobox(
    training_frame,
    values=["Beginner", "Intermediate", "Advanced"],
    width=22,
    state="readonly"
)
skill_level_combo.grid(row=1, column=1, padx=10, pady=5)

tk.Label(training_frame, text="Completion Date:", bg="white", font=("Arial", 11)).grid(row=1, column=2, sticky="w", pady=5)
completion_entry = tk.Entry(training_frame, width=25)
completion_entry.grid(row=1, column=3, padx=10, pady=5)

tk.Label(training_frame, text="Certification:", bg="white", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=5)
cert_entry = tk.Entry(training_frame, width=25)
cert_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(training_frame, text="Renewal Date:", bg="white", font=("Arial", 11)).grid(row=2, column=2, sticky="w", pady=5)
renewal_entry = tk.Entry(training_frame, width=25)
renewal_entry.grid(row=2, column=3, padx=10, pady=5)

tk.Button(
    training_frame,
    text="Add Training Record",
    font=("Arial", 11, "bold"),
    bg="#16a34a",
    fg="white",
    width=20,
    command=save_training
).grid(row=3, column=0, columnspan=4, pady=15)

# ----------------------------
# Employees Table
# ----------------------------
employee_table_frame = tk.LabelFrame(
    root,
    text="Employees",
    font=("Arial", 12, "bold"),
    bg="white",
    padx=10,
    pady=10
)
employee_table_frame.pack(fill="both", expand=True, padx=20, pady=10)

employee_columns = ("Employee ID", "Name", "Department", "Job Role")
employee_tree = ttk.Treeview(employee_table_frame, columns=employee_columns, show="headings", height=8)

for col in employee_columns:
    employee_tree.heading(col, text=col)
    employee_tree.column(col, width=150)

employee_tree.pack(fill="both", expand=True)

# ----------------------------
# Training Records Table
# ----------------------------
training_table_frame = tk.LabelFrame(
    root,
    text="Training Records",
    font=("Arial", 12, "bold"),
    bg="white",
    padx=10,
    pady=10
)
training_table_frame.pack(fill="both", expand=True, padx=20, pady=10)

training_columns = (
    "Record ID", "Employee ID", "Employee Name",
    "Skill", "Level", "Completion Date",
    "Certification", "Renewal Date"
)

training_tree = ttk.Treeview(training_table_frame, columns=training_columns, show="headings", height=8)

for col in training_columns:
    training_tree.heading(col, text=col)
    training_tree.column(col, width=130)

training_tree.pack(fill="both", expand=True)

# ----------------------------
# Load existing data
# ----------------------------
load_employees()
load_training_records()

root.mainloop()
