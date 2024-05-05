import random
from updater import max_baid, csv_writer_balance
import csv
from bankcard import Bankcard
from format import *
from transaction import Transaction

class BankAccount:
    def __init__(self, accountnum: str, balance: int, bankcard: Bankcard, transactions: list, baid: int):
        self.__accountnum = accountnum
        self.__balance = balance
        self.__bankcard = bankcard
        self.__transactions = transactions
        self.__baid = baid

    @property
    def baid(self):
        return self.__baid
    @property
    def transactions(self):
        return self.__transactions
    @property
    def bankcard(self):
        return self.__bankcard
    @property
    def balance(self):
        return self.__balance
    @property
    def accountnum(self):
        return self.__accountnum

    @bankcard.setter
    def bankcard(self, value):
        self.__bankcard = value

    @transactions.setter
    def transactions(self, value):
        self.__transactions = value

    def create_ba(self):

        accountnumber = random.randint(221000000000000000, 221099999999999999)
        balance = 0
        bankcard = Bankcard(None, None, None, None, None)
        bankcard = Bankcard.create_bankcard(bankcard)
        bcnum = bankcard.cardnum
        transactions = []
        baid = max_baid()+1
        newba = BankAccount(accountnumber, balance, bankcard, transactions, baid)
        newbadata = [accountnumber, balance, bcnum, transactions, baid]
        with open("bankaccounts.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(newbadata)

        return newba


    def __str__(self):
        return f"{BLUE}Számlaszám: {RESET}{YELLOW}{self.__accountnum}{RESET}\n{BLUE}Egyenleg: {RESET}{YELLOW}{self.__balance}{RESET}\n{BLUE}Trancakciók: {RESET}{YELLOW}{len(self.__transactions)} db{RESET}\n{BLUE}Bankszámla ID: {RESET}{YELLOW}{self.__baid}{RESET}\n----------\n{BLUE}{BOLD}Bankkártya adatai:{RESET}\n{YELLOW}{self._BankAccount__bankcard}{RESET}"

    def mplus(self, amount, sid):
        base = self.__balance
        new_balance = int(base) + int(amount)
        self.__balance = new_balance
        new_transaction = Transaction(None, None, None, None, None)
        new_transaction = Transaction.create_transaction(new_transaction, sid, amount, "+")
        print(f"plussid: {sid}")
        csv_writer_balance(sid, new_balance)


    def mminus(self, amount, sid):

        base = self.__balance
        new_balance = int(base) - int(amount)
        self.__balance = new_balance
        new_transaction = Transaction(None, None, None, None, None)
        new_transaction = Transaction.create_transaction(new_transaction, sid, amount, "-")
        print(f"minussid: {sid}")
        csv_writer_balance(sid, new_balance)
