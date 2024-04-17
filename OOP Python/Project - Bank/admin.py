from person import Person
class Admin(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int, adminid: int):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__adminid = adminid

    @property
    def adminid(self):
        return  self.__adminid


    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nAdmin ID: {self.__adminid}"
    def data_updater(self):
        super().data_updater()