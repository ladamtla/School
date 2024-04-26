from person import Person
from format import *
from updater import csv_writer
import time
class Employee(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int,empId: int):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__empId = empId

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nEmployee ID: {self.__empId}"

    def data_updater(self):
        super().data_updater()
        csv_writer("Peoples/customers.csv", self._Person__pid, [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None])
        print(f"{GREEN}Az adatmódosítás sikeres!{RESET}")
        time.sleep(1)