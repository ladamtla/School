import time
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator, usernamevalidator, passwdvalidator
from format import *
from updater import updater
from updater import max_id



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

    @property
    def passwd(self):
        return self.__passw

    @property
    def pid(self):
        return self.__pid

    @property
    def sid(self):
        return self.__sid

    @property
    def username(self):
        return self.__username


    def create_person(self):
        newperson = None


    def data_updater(self):
        while True:
            try:
                selector = input(
                    f"{CYAN}1 - Összes adat\n2 - Név\n3 - Telefonszám\n4 - E-mail cím\n5 - Település\n6 - Jelszó{RESET}\nMilyen adato(ka)t szeretne módosítani?: ")
                if selector == "1":
                    self.__name = namevalidator()
                    self.__phone = phonevalidator()
                    self.__email = emailvalidator()
                    self.__city = cityvalidator()
                    self.__passw = passwdvalidator()
                    break
                elif selector == "2":
                    self.__name = namevalidator()
                    break
                elif selector == "3":
                    self.__phone = phonevalidator()
                    break
                elif selector == "4":
                    self.__email = emailvalidator()
                    break
                elif selector == "5":
                    self.__city = cityvalidator()
                    break
                elif selector == "6":
                    self.__passw = passwdvalidator()
                    break
                else:
                    print(f"{RED}Hibás menüpont!{RESET}")
                    time.sleep(1)
            except:
                continue

    def pass_updater(self):
            self.__passw = passwdvalidator()




    def __str__(self):
        return f"Név: {self.__name}\nTelefonszám: {self.__phone}\nE-mail cím: {self.__email}\nTelepülés: {self.__city}\nFelhasználónév: {self.__username}\nJelszó: {self.__passw}\nPerson ID: {self.__pid}"