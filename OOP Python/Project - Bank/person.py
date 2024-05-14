import time
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator, passwdvalidator
from format import *

class Person:
    """
    Person alap osztály deffiniálása az alap adatokkal.
    """
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
        """
        Adatmódosító metódus. Lehetőség van az adatokat egysezrre, vagy külön külön is módosítani.
        """
        while True:
            try:
                print(" ")
                selector = input(
                    f"{CYAN}1 - All data\n2 - Name\n3 - Phone number\n4 - E-mail address\n5 - Place of settlement\n6 - Password{RESET}\nWhich data would you like to modify?: ")
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
                    print(f"{RED}Wrong menu option!{RESET}")
                    time.sleep(1)
            except:
                continue

    def pass_updater(self):
        """
        Frissíti a jelszót az adott objektumnál
        """
        self.__passw = passwdvalidator()




    def __str__(self)->str:
        """
        Adatok formázása szövegbe.
        :param self: objektum
        :return: formázott szöveg
        """
        return f"{BLUE}Name: {RESET}{YELLOW}{self.__name}{RESET}\n{BLUE}Phone number: {RESET}{YELLOW}{self.__phone}{RESET}\n{BLUE}E-mail address: {RESET}{YELLOW}{self.__email}{RESET}\n{BLUE}Place of settlement: {RESET}{YELLOW}{self.__city}{RESET}\n{BLUE}Username: {RESET}{YELLOW}{self.__username}{RESET}\n{BLUE}Password: {RESET}{YELLOW}{self.__passw}{RESET}\n{BLUE}Person ID: {RESET}{YELLOW}{self.__pid}{RESET}"