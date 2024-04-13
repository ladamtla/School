from person import Person
class Customer(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, customerId: int):
        super().__init__(name, phone, email, city, username, passw)
        self.customerId = customerId

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nCustomer ID: {self.customerId}"