import random
from datetime import datetime
from format import *
import csv

def expdate_generator()->str:
    """
    Lejárati dátum random generáló függvény. 3 és 5 év között, a jelenlegi dátumtól.
    :return: Lejárati dátum "/" jellel formázottan
    """
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
    """
    Bankkártya osztály deffiniálása.
    """
    def __init__(self, cardnum: int, expdate: str, cvv: int, brand: str, rfidtag: int):
        self.__cardnum = cardnum
        self.__expdate = expdate
        self.__cvv = cvv
        self.__brand = brand
        self.__rfidtag = rfidtag

    @property
    def cardnum(self):
        return  self.__cardnum

    @property
    def expdate(self):
        return  self.__expdate

    @property
    def cvv(self):
        return  self.__cvv

    @property
    def brand(self):
        return  self.__brand

    @property
    def rfidtag(self):
        return  self.__rfidtag

    def __str__(self):
        """
        Adatok formázása szövegbe.
        :return: formázott szöveg
        """
        cardnum_str = str(self.__cardnum)
        cardnum1 = cardnum_str[0:4]
        cardnum2 = cardnum_str[4:8]
        cardnum3 = cardnum_str[8:12]
        cardnum4 = cardnum_str[12:16]
        return f"{BLUE}Card number:{RESET} {YELLOW}{cardnum1} {cardnum2} {cardnum3} {cardnum4} {RESET}\n{BLUE}Expiration date: {RESET}{YELLOW}{self.__expdate}{RESET}\n{BLUE}CVV number: {RESET}{YELLOW}{self.__cvv}{RESET}\n{BLUE}Brand: {RESET}{YELLOW}{self.__brand}{RESET}\n{BLUE}RFID tag: {RESET}{YELLOW}{self.__rfidtag}{RESET}"

    def create_bankcard(self):
        """
        Bankkártya létrehozás, autómatikusan lefut bankszámla létrehozásakor, rékérdez a kártya márkájára.
        :return: Létrehozott Bankcard objektum
        """
        while True:
            try:
                brand = input(f"{CYAN}1 - Visa\n2 - MasterCard{RESET}\n{ITALIC}{YELLOW}Card brand: {RESET}")
                if brand == "1":
                    brand = "VISA"
                    cardnum = random.randint(4000000000000000, 4999999999999999)
                    break
                elif brand == "2":
                    brand = "MASTERCARD"
                    cardnum = random.randint(5000000000000000, 5999999999999999)
                    break
                else:
                    print("Wrong input!")
            except:
                continue
        expdate = expdate_generator()
        cvv = random.randint(100, 999)
        rfidtag = random.randint(1000000000000000, 9999999999999999)

        bcdata = [cardnum ,expdate, cvv, brand, rfidtag]
        with open("data/bankcards.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(bcdata)

        return Bankcard(cardnum, expdate, cvv, brand, rfidtag)




