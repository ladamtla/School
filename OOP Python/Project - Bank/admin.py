from person import Person
from updater import csv_writer
import time
from format import *



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
        csv_writer("Peoples/admins.csv", self._Person__pid, [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None])
        print(f"{GREEN}Az adatmódosítás sikeres!{RESET}")
        time.sleep(1)