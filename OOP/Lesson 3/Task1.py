class Employee:
    def __init__(self, name: str, age: int, email: str, title: str):
        self.name = name
        self.age = age
        self.email = email
        self.title = title

    def __del__(self):
        print(f"{self.name} deleted")

def read_employees(filename: str) -> list[Employee]:
    emp_file = open(filename, "r")
    lines = emp_file.readlines()
    lines.pop(0)
    employees: list[Employee] = []
    for line in lines:
        line.replace("\n", "")
        print(line)
        split_line = line.split(",")
        emp = Employee( split_line[0], int(split_line[1]), split_line[2], split_line[3])
        employees.append(emp)
    emp_file.close()
    return employees

def find_employee(employees: list[Employee], name: str):
    for emp in employees:
        if emp.name == nem:
            return emp
    return None

def print_employees(emp: list[Employee]):
    for emp in emp:
        print(f"{emp.name}\n\t{emp.age}\n\t{emp.email}\n\t{emp.title}")

def main():
    employees = read_employees("employee.csv")
    print_employees(employees)
    name = input("Name: ")
    emp = find_employee(employees, name)
    if emp is not None:
        for i in emps:
            print_employees(emp)
        else:
            print("None")

if __name__ == "__main__":
    main()
