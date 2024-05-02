import random
from updater import max_baid
import csv
from bankcard import Bankcard

class BankAccount:
    def __init__(self, accountnum: str, balance: int, bankcards: [Bankcard], transactions: list, baid: int):
        self.__accountnum = accountnum
        self.__balance = balance
        self.__bankcards = bankcards
        self.__transactions = transactions
        self.__baid = baid

    @property
    def baid(self):
        return self.__baid
    @property
    def transactions(self):
        return self.__transactions
    @property
    def bankcards(self):
        return self.__bankcards
    @property
    def balance(self):
        return self.__balance
    @property
    def accountnum(self):
        return self.__accountnum

    def create_ba(self):

        accountnumber = random.randint(221000000000000000000000, 221099999999999999999999)
        balance = 0
        bankcards = []
        transactions = []
        baid = max_baid()+1

        newba = BankAccount(accountnumber, balance, bankcards, transactions, baid)
        newbadata = [accountnumber, balance, bankcards, transactions, baid]
        with open("bankaccounts.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(newbadata)

        return newba


    def __str__(self):
        return f"Számlaszám: {self.__accountnum}\nEgyenleg: {self.__balance}\nBankkártyák: {self.__bankCards}\nTrancakciók: {self.__transactions}\nBankszámla ID: {self.__baid}"