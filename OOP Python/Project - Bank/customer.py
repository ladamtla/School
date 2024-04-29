from person import Person
from format import *
from updater import csv_writer
import time
import csv
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator
from updater import max_id
from bankaccount import BankAccount
class Customer(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int, customerId: int, bankaccount: BankAccount):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__customerId = customerId
        self.__bankaccount = bankaccount

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nBankszámla: {self.__bankcards}\nCustomer ID: {self.__customerId}"


    def create_person(self):
        name = namevalidator()
        phone = phonevalidator()
        email = emailvalidator()
        city = cityvalidator()
        username = name[:5] + phone[-3:]
        passw = "123456789"
        maxpid = max_id(0)
        pid = maxpid + 1
        maxcustomerid = max_id(3)
        customerid = maxcustomerid + 1
        ba = None
        newperson = Customer(name, phone, email, city, username, passw, pid, customerid, ba)
        newcustomerdata = [name, phone, email, city, username, passw, pid, customerid, ba]
        with open("Peoples/customers.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(newcustomerdata)
        super().create_person()
        return newperson

    def data_updater(self):
        super().data_updater()
        csv_writer("Peoples/customers.csv", self._Person__pid, [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None, None])
        print(f"{GREEN}Az adatmódosítás sikeres!{RESET}")
        time.sleep(1)
