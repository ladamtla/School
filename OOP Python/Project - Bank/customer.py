from person import Person
from format import *
from updater import csv_writer
import time
import csv
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator, passwdvalidator
from updater import max_id
from bankaccount import BankAccount
from bankcard import Bankcard

class Customer(Person):
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int, sid: int, bankaccount: BankAccount):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__sid = sid
        self.__bankaccount = bankaccount


    @property
    def username(self):
        return self._Person__username

    @property
    def passw(self):
        return self._Person__passw

    @property
    def sid(self):
        return self.__sid

    @property
    def bankaccount(self):
        return self.__bankaccount


    def __str__(self):
        base_info = super().__str__()
        return (f"{base_info}\n{BLUE}Customer ID: {RESET}{YELLOW}{self.__sid}{RESET}\n----------\n{BLUE}{BOLD}Bankszámla adatai:{RESET}\n{self.__bankaccount}")


    def create_person(self):
        name = namevalidator()
        phone = phonevalidator()
        email = emailvalidator()
        city = cityvalidator()
        username = name[:5] + phone[-3:]
        passw = passwdvalidator()
        maxpid = max_id(0)
        pid = maxpid + 1
        maxsid = max_id(3)
        sid = maxsid + 1
        bc = Bankcard(None, None, None, None, None)
        print(f"{YELLOW}{ITALIC}Bankkártya létrehozása:{RESET}")
        ba = BankAccount(None, None, None, None, None)
        ba = BankAccount.create_ba(ba)
        time.sleep(1)
        print(f"{GREEN}Bankkártya létrehozva!{RESET}")
        time.sleep(1)
        print(f"{YELLOW}{ITALIC}Bankszámla létrehozása...")
        time.sleep(1)
        print(f"{GREEN}Bankszámla létrehozva!{RESET}")
        with open(f"Transactiondata/{sid}.csv", mode='x'):
            pass
        newperson = Customer(name, phone, email, city, username, passw, pid, sid, ba)
        newcustomerdata = [name, phone, email, city, username, passw, pid, sid, ba.baid]
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

    def ba_append(self, ba):
        print(ba)
        self.__bankaccount = ba
        baid = ba.baid
        csv_writer("Peoples/customers.csv", self._Person__pid,[None, None, None, None, None, None, None, None, baid])
        print(f"{GREEN}Bankszámla sikeresen létrehozva!{RESET}")
        time.sleep(1)

    def transfer(self, sid, tsid, amount, bankaccounts):
        print("Custtrans1")
        BankAccount.mminus(bankaccounts[sid-1], amount, sid)
        print("Custtrans2")
        BankAccount.mplus(bankaccounts[tsid-1], amount, tsid)
