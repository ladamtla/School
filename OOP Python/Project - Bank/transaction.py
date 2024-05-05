from datetime import datetime
from updater import max_trid
import csv
from format import *

class Transaction:
    def __init__(self, tranID: int, date: str, time: str, amount: int, type: str):
        self.__tranID = tranID
        self.__date = date
        self.__time = time
        self.__amount = amount
        self.__type = type


    def create_transaction(self, sid, amount, type):
        print(sid)
        print(max_trid(sid))
        self.__tranID = int(max_trid(sid))+1
        self.__amount = int(amount)
        self.__type = type
        self.__date = datetime.now().date()
        self.__time = datetime.now().time()
        trdata = [self.__tranID, self.__date, self.__time, amount, type]
        filename = f"Transactiondata/{sid}.csv"
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(trdata)


    def __str__(self):
        return f"{BLUE}ID:{RESET} {YELLOW}{self.__tranID}{RESET} | {BLUE}Dátum:{RESET} {YELLOW}{self.__date}{RESET} | {BLUE}Idő:{RESET} {YELLOW}{self.__time}{RESET} | {BLUE}Összeg:{RESET} {YELLOW}{self.__amount}{RESET} | {BLUE}Típus:{RESET} {YELLOW}{self.__type}{RESET}"