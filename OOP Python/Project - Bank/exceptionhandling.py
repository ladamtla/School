import re
import csv
from format import *

def namevalidator():
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

def phonevalidator():
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
    pattern = r"^[a-zA-Z0-9-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
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