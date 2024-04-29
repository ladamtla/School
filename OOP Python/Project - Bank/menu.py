from format import *
import time
from employee import Employee

def login(admins, employees, customers):
    while True:
        try:
            selector = input(
                f"{CYAN}1 - Admin\n2 - Banki alkalmazott\n3 - Felhasználó{RESET}\nVálasszon fióktípust a bejelentkezéshez!: ")
            if selector == "1":
                pid = loginto(admins)
                break
            elif selector == "2":
                pid = loginto(employees)
                break
            elif selector == "3":
                pid = loginto(customers)
                break
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue
    print(pid)
    print(selector)
    return pid, selector

def loginto(persons):
    while True:
        try:
            username = input(f"{YELLOW}{ITALIC}Felhasználónév: {RESET}")
            for person in persons:
                pid = person.pid
                if username == person.username:
                    pass_validator(person.passwd)
                    break
                else:
                    print(f"{RED}Hibás felhasználónév!{RESET}")
            break
        except:
            continue
    return pid

def pass_validator(passwd):
    while True:
        try:
            inpass = input(f"{YELLOW}{ITALIC}Jelszó: {RESET}")
            if inpass == passwd:
                print(f"{GREEN}Sikeres bejelentkezés!{RESET}")
                break
            else:
                print(f"{RED}Hibás jelszó!{RESET}")
        except:
            continue

def mainmenu(pid, selector):
    if selector == 0:
        adminmenu(pid)
    elif selector == 1:
        empmenu(pid)
    elif selector == 2:
        customermenu(pid)

def adminmenu(pid):
    while True:
        try:
            selector = input(
                f"{CYAN}1 - Új dolgozó létrehozása\n2 - 2. opció\n3 - 3. opció{RESET}\nVálasszon műveletet: ")
            if selector == "1":
                Employee.create_person()
                break
            elif selector == "2":
                pass
                break
            elif selector == "3":
                pass
                break
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue
    return pid

def empmenu(pid):
    pass

def customermenu(pid):
    pass


