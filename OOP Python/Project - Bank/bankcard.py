import random
from enum import Enum
from datetime import datetime
from format import *

def expdate_generator():
    expdate = datetime.now()
    expdate = str(expdate)
    year = expdate[2:4]
    month = expdate[5:7]
    year = int(year)
    expdate = year + random.randint(3, 5)
    expdate = str(expdate)
    expdate = month + "/" + expdate
    return expdate

class Bankcard:
    def __init__(self, cardnum: int, expdate: str, cvv: int, brand: str, rfidtag: int):
        self.__cardnum = cardnum
        self.__expdate = expdate
        self.__cvv = cvv
        self.__brand = brand
        self.__rfidtag = rfidtag

    def __str__(self):
        cardnum_str = str(self.__cardnum)
        cardnum1 = cardnum_str[0:4]
        cardnum2 = cardnum_str[4:8]
        cardnum3 = cardnum_str[8:12]
        cardnum4 = cardnum_str[12:16]
        return f"Kártyaszám: {cardnum1} {cardnum2} {cardnum3} {cardnum4} \nLejárati dátum: {self.__expdate}\nCVV kód: {self.__cvv}\nMárka: {self.__brand}\nRFID tag: {self.__rfidtag}"

    def create_bankcard(cls, name):
        while True:
            try:
                brand = input(f"1 - Visa\n2 - MasterCard\n{ITALIC}{YELLOW}Kártya kibocsátó: {RESET}")
                if brand == "1":
                    brand = "VISA"
                    cardnum = random.randint(4000000000000000, 4999999999999999)
                    break
                elif brand == "2":
                    brand = "MASTERCARD"
                    cardnum = random.randint(5000000000000000, 5999999999999999)
                    break
                else:
                    print("Hibás adat!")
            except:
                continue
        expdate = expdate_generator()
        cvv = random.randint(100, 999)
        rfidtag = random.randint(1000000000000000, 9999999999999999)

        return cls(cardnum, expdate, cvv, brand, rfidtag)




