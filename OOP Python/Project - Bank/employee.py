from person import Person
from format import *
from updater import csv_writer
import csv
import time
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator, passwdvalidator
from updater import max_id
class Employee(Person):
    """
    Employee osztály deffiniálása a Person osztályból.
    """
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int,sid: int):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__sid = sid


    @property
    def username(self)->str:
        return self._Person__username

    @property
    def passw(self)->str:
        return self._Person__passw

    @property
    def sid(self)->int:
        return self.__sid


    def __str__(self)->str:
        """
        Adatok formázása szövegbe, használva a Person-nál meghatározottat + kiegészítve az Employee osztályéval.
        :return: formázott szöveg
        """
        base_info = super().__str__()
        return f"{base_info}\n{BLUE}Employee ID: {RESET}{YELLOW}{self.__sid}{RESET}"

    def create_person(self):
        """
        Új employee létrehozása. Egyessével ellenőrzötten bekéri az adatokat.
        :return: Employee típustú objektum
        """
        super().create_person()
        name = namevalidator()
        phone = phonevalidator()
        email = emailvalidator()
        city = cityvalidator()
        username = name[:5] + phone[-3:]
        passw = passwdvalidator()
        maxpid = max_id(0)
        pid = maxpid + 1
        maxempid = max_id(2)
        sid = maxempid + 1
        newperson = Employee(name, phone, email, city, username, passw, pid, sid)
        newempdata = [name, phone, email, city, username, passw, pid, sid]
        with open("People/employees.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(newempdata)
        return newperson


    def data_updater(self):
        """
        Frissíti az Employee objektumok adatait az employees.csv fileban.
        """
        super().data_updater()
        csv_writer("People/employees.csv", self._Person__pid, [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None])
        print(f"{GREEN}Data modification successful!{RESET}")
        time.sleep(1)