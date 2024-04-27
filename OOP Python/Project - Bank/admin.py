from person import Person
from updater import csv_writer, max_id
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator, usernamevalidator, passwdvalidator
import time
import csv
from format import *



class Admin(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int, adminid: int):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__adminid = adminid

    @property
    def username(self):
        return self._Person__username

    @property
    def passw(self):
        return self._Person__passw

    @property
    def adminid(self):
        return self.__adminid


    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nAdmin ID: {self.__adminid}"

    def create_person(self):
        super().create_person()
        name = namevalidator()
        phone = phonevalidator()
        email = emailvalidator()
        city = cityvalidator()
        username = name[:5] + phone[-3:]
        passw = "123456789"
        maxpid = max_id(0)
        pid = maxpid + 1
        maxadminid = max_id(1)
        adminid = maxadminid + 1
        newperson = Admin(name, phone, email, city, username, passw, pid, adminid)
        newadmindata = [name, phone, email, city, username, passw, pid, adminid]
        with open("Peoples/admins.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(newadmindata)

        return newperson

    def data_updater(self):
        super().data_updater()
        csv_writer("Peoples/admins.csv", self._Person__pid, [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None])
        print(f"{GREEN}Az adatmódosítás sikeres!{RESET}")
        time.sleep(1)