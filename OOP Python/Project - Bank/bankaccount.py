import random
from updater import max_baid
import csv

class BankAccount:
    def __init__(self, accountNum: str, balance: int, bankCards: list, transactions: list, baID: int):
        self.__accountnum = accountNum
        self.__balance = balance
        self.__bankCards = bankCards
        self.__transactions = transactions
        self.__baiID = baID

    @property
    def baid(self):
        return self.__baiID

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
        return f"Számlaszám: {self.__accountnum}\nEgyenleg: {self.__balance}\nBankkártyák: {self.__bankCards}\nTrancakciók: {self.__transactions}\nBankszámla ID: {self.__baiID}"