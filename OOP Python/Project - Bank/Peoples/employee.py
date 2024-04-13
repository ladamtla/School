from person import Person
class Employee(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, empId: int):
        super().__init__(name, phone, email, city, username, passw)
        self.empId = empId

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nEmployee ID: {self.empId}"