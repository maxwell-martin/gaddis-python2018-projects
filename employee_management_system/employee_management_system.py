import employee, pickle

EMPLOYEE_FILE_NAME = "employees.dat"

def get_choice():
    display_menu()
    try:
        choice = int(input("Enter a choice: "))
        if choice in range(1,6):
            return choice
        else:
            raise Exception
    except Exception:
        print("\nInvalid choice. Please enter an integer between 1-5.")

def display_menu():
    print()
    print("---Employee Management System---")
    print("(1) Look up an employee")
    print("(2) Add a new employee")
    print("(3) Change an existing employee's information")
    print("(4) Delete an employee")
    print("(5) Quit the program")
    print("--------------------------------")
    print()

def load_employees(file_name):
    try:
        with open(file_name, "rb") as infile:
            employees = pickle.load(infile)
    except:
        employees = {}
    return employees

def save_employees(employees, file_name):
    try:
        with open(file_name, "wb") as outfile:
            pickle.dump(employees, outfile)
        print("\nEmployee information saved. Goodbye.")
    except:
        print("\nError saving employee information. Goodbye.")

def lookup(employees):
    id_number = input("Enter employee ID: ")
    print()
    print(employees.get(id_number, "An employee with ID " + \
                        id_number + " was not found."))

def add(employees):
    id_number = input("Enter employee ID: ")
    if id_number not in employees.keys():
        name = input("Enter employee's name: ")
        department = input("Enter employee's department: ")
        job_title = input("Enter employee's job title: ")
        emp = employee.Employee(name, id_number, department, job_title)
        employees[id_number] = emp
        print("\nID: " + id_number + " - " + name + " has been added.")
    else:
        print("\nAn employee with ID:", id_number, "already exists.")
    return employees

def change(employees):
    id_number = input("Enter employee ID: ")
    if id_number in employees.keys():
        name = input("Enter employee's new name: ")
        department = input("Enter employee's new department: ")
        job_title = input("Enter employee's new job title: ")
        emp = employee.Employee(name, id_number, department, job_title)
        employees[id_number] = emp
        print("\nID: " + id_number + " - " + name + " has been updated.")
    else:
        print("\nAn employee with ID:", id_number, "does not exist.")
    return employees

def delete(employees):
    id_number = input("Enter employee ID: ")
    if id_number in employees.keys():
        del employees[id_number]
        print("\nEmployee with ID:", id_number, "has been deleted.")
    else:
        print("\nAn employee with ID:", id_number, "does not exist.")
    return employees

def main():
    employees = load_employees(EMPLOYEE_FILE_NAME)
    choice = None
    while choice != 5:
        choice = get_choice()
        if choice == 1:
            lookup(employees)
        elif choice == 2:
            employees = add(employees)
        elif choice == 3:
            employees = change(employees)
        elif choice == 4:
            employees = delete(employees)

    save_employees(employees, EMPLOYEE_FILE_NAME)

main()
