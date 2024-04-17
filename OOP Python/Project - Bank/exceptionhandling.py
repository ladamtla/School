import re
import csv

RED = "\033[31m"
RESET = "\033[0m"

def namevalidator():
    while True:
        try:
            name = input("Teljes név: ")
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
            phone = input("Telefonszám (+36123456789): ")
            if re.match(pattern, phone):
                break
            else:
                print(f"{RED}Hibás formátum!{RESET}")
        except:
            continue
    return phone

def emailvalidator():
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    while True:
        try:
            email = input("Email cím: ")
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
            city = input("Település: ")
            if city in cities_set:
                return city
            else:
                print(f"{RED}Valós, magyar településnevet adjon meg!{RESET}")
        except:
            continue

def usernamevalidator():
    pattern = "^[a-zA-Z0-9]{5,}$"
    while True:
        try:
            username = input("Felhasználónév: ")
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
            passwd = input("Jelszó: ")
            if len(passwd) > 7 and re.search(r'[a-z]', passwd) and re.search(r'[A-Z]', passwd) and re.search(r'\d', passwd) and re.search(r'[!#$%&*+?@]', passwd):
                break
            else:
                print(f"{RED}Hibás formátum! (Minimum hosszúság: 8 karakter, Tartalmaznia kell: kisbetű, nagybetű, szám, speciális karakter(!,#,$,%,&,*,+,?,@)){RESET}")
        except:
            continue
    return passwd