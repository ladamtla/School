from person import Person
from format import *
from updater import csv_writer
import time
class Customer(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int, customerId: int, bankcards: list):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__customerId = customerId
        self.__bankcards = bankcards

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nBankkártyák: {self.__bankcards}\nCustomer ID: {self.__customerId}"

    def data_updater(self):
        super().data_updater()
        csv_writer("Peoples/customers.csv", self._Person__pid, [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None, None])
        print(f"{GREEN}Az adatmódosítás sikeres!{RESET}")
        time.sleep(1)
