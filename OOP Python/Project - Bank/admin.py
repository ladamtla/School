from person import Person
class Admin(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, adminId: int):
        super().__init__(name, phone, email, city, username, passw)
        self.adminId = adminId

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nAdmin ID: {self.adminId}"
    def data_updater(self):
        super().data_updater()