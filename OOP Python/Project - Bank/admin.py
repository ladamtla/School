from person import Person
from updater import csv_writer, max_id
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator, passwdvalidator
import time
import csv
from format import *



class Admin(Person):
    """
    Admin osztály deffiniálása a Person osztályból.
    """
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int, sid: int):
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
        Adatok formázása szövegbe, használva a Person-nál meghatározottat + kiegészítve az Admin osztályéval.
        :return: formázott szöveg
        """
        base_info = super().__str__()
        return f"{base_info}\n{BLUE}Admin ID: {RESET}{YELLOW}{self.__sid}{RESET}"

    def create_person(self):
        """
        Új admin létrehozása. Egyessével ellenőrzötten bekéri az adatokat.
        :return: Admin típustú objektum
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
        maxsid = max_id(1)
        adminid = maxsid + 1
        newperson = Admin(name, phone, email, city, username, passw, pid, adminid)
        newadmindata = [name, phone, email, city, username, passw, pid, adminid]
        with open("People/admins.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(newadmindata)

        return newperson


    def data_updater(self):
        """
        Frissíti az Admin objektumok adatait az admins.csv fileban.
        """
        super().data_updater()
        csv_writer("People/admins.csv", self._Person__pid, [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None])
        print(f"{GREEN}Data modification successful!{RESET}")
        time.sleep(1)