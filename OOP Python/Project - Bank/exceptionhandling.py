import re
import csv
from format import *

def namevalidator()->str:
    """
    Ellenőrzötten beolvas egy nevet, majd visszadja azt. Legalább egy " " karektert tartalmaznia kell.
    :return: név szövegként
    """
    while True:
        try:
            name = input(f"{ITALIC}{YELLOW}Teljes név: {RESET}")
            if " " in name:
                break
            else:
                print(f"{RED}Teljes nevet adjon meg!{RESET}")
        except:
            continue
    return name

def phonevalidator()->str:
    """
    Ellenőrzötten beolvas egy telefonszámot, majd visszadja azt. "+" jellel kell, hoyg kezdődjön és legalább 10 karakter hosszó legyen.
    :return: telefonszám szövegként
    """
    pattern = r"^\+[0-9]{10,}$"
    while True:
        try:
            phone = input(f"{ITALIC}{YELLOW}Telefonszám (+36123456789): {RESET}")
            if re.match(pattern, phone):
                break
            else:
                print(f"{RED}Hibás formátum!{RESET}")
        except:
            continue
    return phone

def emailvalidator():
    """
    Ellenőrzötten beolvas egy emailcímet, majd visszadja azt. valami@valami.valami formátum
    :return:
    """
    pattern = r"^[a-zA-Z0-9-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$"
    while True:
        try:
            email = input(f"{ITALIC}{YELLOW}Email cím: {RESET}")
            if re.match(pattern, email):
                break
            else:
                print(f"{RED}Hibás formátum!{RESET}")
        except:
            continue
    return email


def cityvalidator():
    """
    Ellenőrzötten beolvas egy település nevet, majd visszadja azt. Elelnőrzi egy csv lista segítségével, hogy a megadott szöveg valóban egy valós Magyar településnév-e.
    :return:
    """

    cities_set = set()
    with open("cdata/hun_cities.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cities_set.add(row[0])

    while True:
        try:
            city = input(f"{ITALIC}{YELLOW}Település: {RESET}")
            if city in cities_set:
                return city
            else:
                print(f"{RED}Valós, Magyar településnevet adjon meg!{RESET}")
        except:
            continue

def usernamevalidator():
    """
    Ellenőrzötten beolvas egy felhasználónevet, majd visszadja azt. kisbetű, nagyvatű, szám lehet benne minimum 5 karakter
    :return:
    """
    pattern = "^[a-zA-Z0-9]{5,}$"
    while True:
        try:
            username = input(f"{ITALIC}{YELLOW}Felhasználónév: {RESET}")
            if re.match(pattern, username):
                break
            else:
                print(f"{RED}Hibás formátum! (Minimum hosszúság: 5 karakter, Megnengedett: kisbetű, nagybetű, szám){RESET}")
        except:
            continue
    return username

def passwdvalidator():
    """
    Ellenőrzötten beolvas egy jelszót, majd visszadja azt. Kell bele: kisbetű, nagybetű, szám, spec. karakter, valamint legalább 8 karakter hosszúság.
    :return:
    """
    while True:
        try:
            passwd = input(f"{ITALIC}{YELLOW}Jelszó: {RESET}")
            if len(passwd) > 7 and re.search(r'[a-z]', passwd) and re.search(r'[A-Z]', passwd) and re.search(r'\d', passwd) and re.search(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', passwd):
                pass
            else:
                print(f"{RED}Hibás formátum! (Minimum hosszúság: 8 karakter, A jelszónak tartalmaznia kell: kisbetű, nagybetű, szám, speciális karakter){RESET}")
                continue
            passwdagain = input(f"{ITALIC}{YELLOW}Jelszó mégegyszer: {RESET}")
            if passwd == passwdagain:
                break
            else:
                print(f"{RED}A két jelszó nem eggyezik!{RESET}")
        except:
            continue
    return passwd