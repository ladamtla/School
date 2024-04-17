import random
from enum import Enum
from datetime import datetime


class CardBrand(Enum):
    VISA = "Visa"
    MASTERCARD = "Mastercard"
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



    def create_bankcard(self, brand):
        while True:
            try:
                brand = input("Kártya kibocsátó: ")
                if brand == "Visa" or "VISA":
                    self.__brand = "VISA"
                    self.__cardnum = random.randint(4000000000000000, 4999999999999999)
                elif brand == "MasterCard" or "MASTERCARD" or "mastercard" or "Mastercard":
                    self.__brand = "MASTERCARD"
                    self.__cardnum = random.randint(5000000000000000, 5999999999999999)
                else:
                    print("Hibás adat!")
            except:
                continue
        self.__expdate =



