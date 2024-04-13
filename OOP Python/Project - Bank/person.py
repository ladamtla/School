class Person:
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.city = city
        self.username = username
        self.passw = passw

    def data_updater(self):
        self.name = input("Név: ")
        self.phone = input("Telefonszám: ")
        self.email = input("Email: ")
        self.city = input("Város: ")
        self.username = input("Felhasználónév: ")

    def __str__(self):
        return f"Név: {self.name}\nTelefonszám: {self.phone}\nE-mail cím: {self.email}\nVáros: {self.city}\nFelhasználónév: {self.username}\nJelszó: {self.passw}"