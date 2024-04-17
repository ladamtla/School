
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator, usernamevalidator, passwdvalidator




class Person:
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__city = city
        self.__username = username
        self.__passw = passw
        self.__pid = pid

    @property
    def name(self):
        return self.__name


    def data_updater(self):
        self.__name = namevalidator()
        self.__phone = phonevalidator()
        self.__email = emailvalidator()
        self.__city = cityvalidator()
        self.__username = usernamevalidator()
        self.__passw = passwdvalidator()

    def __str__(self):
        return f"Név: {self.__name}\nTelefonszám: {self.__phone}\nE-mail cím: {self.__email}\nTelepülés: {self.__city}\nFelhasználónév: {self.__username}\nJelszó: {self.__passw}\nPerson ID: {self.__pid}"