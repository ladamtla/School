from person import Person
from format import *
from updater import csv_writer
import csv
import time
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator
from updater import max_id
class Employee(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int,empId: int):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__empId = empId

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nEmployee ID: {self.__empId}"

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
        maxempid = max_id(2)
        empid = maxempid + 1
        newperson = Employee(name, phone, email, city, username, passw, pid, empid)
        newempdata = [name, phone, email, city, username, passw, pid, empid]
        with open("Peoples/employees.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(newempdata)
        return newperson


    def data_updater(self):
        super().data_updater()
        csv_writer("Peoples/customers.csv", self._Person__pid, [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None])
        print(f"{GREEN}Az adatmódosítás sikeres!{RESET}")
        time.sleep(1)