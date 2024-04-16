from employee import Employee
from department import Department


class DepartmentReader:
    def __init__(self):
        pass

    def read_input(self, prompt, type_=str, condition=None):
        while True:
            try:
                value = type_(input(prompt))
                if condition and not condition(value):
                    print("Hibás bevitel")
                return value
            except:
                print(f"Hibás bevitel")

    def create_department(self):
        print("Részleg adatai:")
        name = self.read_input("Részleg neve: ")
        print("\nRészlegvezető adatai:")
        head_name = self.read_input("Név: ")
        head_birthdate = self.read_input("Születési dátum (YYYY-MM-DD): ")
        head_salary = self.read_input("Fizetés: ", type_=float)
        head = Employee(head_name, head_birthdate, head_salary)

        department = Department(name, head)

        return department


