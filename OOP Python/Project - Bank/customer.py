from person import Person
from format import *
from updater import csv_writer, read_transactions
import time
import csv
from exceptionhandling import namevalidator, phonevalidator, emailvalidator, cityvalidator, passwdvalidator
from updater import max_id
from bankaccount import BankAccount
from bankcard import Bankcard
from transaction import Transaction

class Customer(Person):
    """
    Customer osztály deffiniálása a Person osztályból.
    """
    def __init__(self, name: str, phone: int, email: str, city: str, username: str, passw: str, pid: int, sid: int, bankaccount: BankAccount):
        super().__init__(name, phone, email, city, username, passw, pid)
        self.__sid = sid
        self.__bankaccount = bankaccount


    @property
    def username(self)->str:
        return self._Person__username

    @property
    def passw(self)->str:
        return self._Person__passw

    @property
    def sid(self)->int:
        return self.__sid

    @property
    def bankaccount(self)->BankAccount:
        return self.__bankaccount


    def __str__(self)->str:
        """
        Adatok formázása szövegbe, használva a Person-nál meghatározottat + kiegészítve az Customer osztályéval.
        :return: formázott szöveg
        """
        base_info = super().__str__()
        return (f"{base_info}\n{BLUE}Customer ID: {RESET}{YELLOW}{self.__sid}{RESET}\n----------\n{BLUE}{BOLD}Bankszámla adatai:{RESET}\n{self.__bankaccount}")


    def create_person(self):
        """
        Új customer létrehozása. Egyessével ellenőrzötten bekéri az adatokat.
        :return: Customer típustú objektum
        """
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
        filename = f"Transactiondata/{sid}.csv"
        with open(filename, 'w') as file:
            file.write("1,2024-01-01,00:00:00.000000,000,+\n")
        newperson = Customer(name, phone, email, city, username, passw, pid, sid, ba)
        newcustomerdata = [name, phone, email, city, username, passw, pid, sid, ba.baid]
        with open("Peoples/customers.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(newcustomerdata)
        super().create_person()
        return newperson

    def data_updater(self):
        """
        Frissíti az Customer objektumok adatait az customers.csv fileban.
        """
        super().data_updater()
        csv_writer("Peoples/customers.csv", int(self._Person__pid), [self._Person__name, self._Person__phone, self._Person__email, self._Person__city, None, self._Person__passw, None, None, None])
        print(f"{GREEN}Az adatmódosítás sikeres!{RESET}")
        time.sleep(1)

    def ba_append(self, ba:BankAccount):
        """
        Hozzárendeli a ba bankszámlát az adott ügyfélhez.
        :param ba: BankAccount típusú objektum
        """
        print(ba)
        self.__bankaccount = ba
        baid = ba.baid
        csv_writer("Peoples/customers.csv", self._Person__pid,[None, None, None, None, None, None, None, None, baid])
        print(f"{GREEN}Bankszámla sikeresen létrehozva!{RESET}")
        time.sleep(1)

    def transfer(self, sid:int, tsid:int, amount:int, bankaccounts:[BankAccount]):
        """
        Átutalás. Egyik ügyfél a másiknak, közben létrejönnek a szükséges tranzakciók objektumként a kívánt helyekre, valamint naplózásra kerülnek a csv fájlokba.
        :param sid: Utaló ügyfél ID száma
        :param tsid: Kedvezményezett ügyfél ID száma
        :param amount: Összeg, amely utalásra kerül
        :param bankaccounts: lista, amely tartalmazza az összes bankszámla objektumot
        """
        mintr = BankAccount.mminus(bankaccounts[sid-1], amount, sid)
        plustr = BankAccount.mplus(bankaccounts[tsid-1], amount, tsid)
        transactions = read_transactions(Transaction, BankAccount)
        print(" ")
        print(f"{YELLOW}Átutalás folyamtban...{RESET}")
        time.sleep(1)
        print(f"{GREEN}Az átutalás teljesült!{RESET}")
        time.sleep(1)
