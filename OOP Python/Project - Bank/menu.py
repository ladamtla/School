from format import *
import time
from employee import Employee
from updater import updater, max_id

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
    return int(pid)

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

def mainmenu(pid, selector, admins, employees, customers):
    print("mainmenu")
    if selector == "1":
        adminmenu(pid, admins, employees)
    elif selector == "2":
        empmenu(pid, employees)
    elif selector == "3":
        customermenu(pid, customers)

def adminmenu(pid, admins, employees):
    print(f"Admin menü {admins[pid-1].name} részére")
    while True:
        try:
            selector = input(
                f"{CYAN}1 - Új dolgozó létrehozása\n2 - Dolgozó adatmódosítás\n3 - 3. opció{RESET}\nVálasszon műveletet: ")
            if selector == "1":
                print("1es")
                new_emp = Employee(None, None, None, None, None, None, None, None)
                new_emp = Employee.create_person(new_emp)
                employees = updater("Peoples/employees.csv", Employee)
                print(f"{GREEN}Új dolgozó sikeresen létrehozva {employees[max_id(2)].name} néven!{RESET}")
                break
            elif selector == "2":
                Employee.data_updater()
                break
            elif selector == "3":
                pass
                break
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue

def empmenu(pid):
    pass

def customermenu(pid):
    pass


