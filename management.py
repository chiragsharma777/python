employees = []

def add_employee():
    print("\n--- Add Employee ---")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    employee = {
        "id": emp_id,
        "name": name,
        "age": age,
        "salary": salary,
        "department": department
    }

    employees.append(employee)

    print("Employee added successfully!")


def show_employees():
    print("\n--- All Employees ---")

    if len(employees) == 0:
        print("No employees found.")
        return

    for emp in employees:
        print("------------------------")
        print("ID         :", emp["id"])
        print("Name       :", emp["name"])
        print("Age        :", emp["age"])
        print("Salary     :", emp["salary"])
        print("Department :", emp["department"])


def search_employee():
    print("\n--- Search Employee ---")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found!")
            print("ID         :", emp["id"])
            print("Name       :", emp["name"])
            print("Age        :", emp["age"])
            print("Salary     :", emp["salary"])
            print("Department :", emp["department"])
            return

    print("Employee not found.")


def delete_employee():
    print("\n--- Delete Employee ---")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully!")
            return

    print("Employee not found.")


def update_salary():
    print("\n--- Update Salary ---")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            new_salary = float(input("Enter new salary: "))
            emp["salary"] = new_salary

            print("Salary updated successfully!")
            return

    print("Employee not found.")


def highest_salary():
    print("\n--- Highest Salary Employee ---")

    if len(employees) == 0:
        print("No employees available.")
        return

    highest = employees[0]

    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp

    print("Name   :", highest["name"])
    print("Salary :", highest["salary"])


while True:

    print("\n==============================")
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Employee")
    print("2. Show All Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Update Salary")
    print("6. Highest Salary")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        show_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        update_salary()

    elif choice == "6":
        highest_salary()

    elif choice == "7":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")