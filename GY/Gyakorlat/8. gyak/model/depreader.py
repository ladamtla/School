import csv
from employee import Employee
from department import Department


class DepartmentReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read_department(self):
        with open(self.filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            department = None
            employees = []

            for row in reader:
                if not department:
                    department_name = row['department_name']
                    head = Employee(row['head_username'], row['head_birthdate'], row['head_salary'])
                    department = Department(department_name, head)

                employee = Employee(row['employee_username'], row['employee_birthdate'], row['employee_salary'])
                department.add_employee(employee)

        return department
