from format import *
import time
from employee import Employee
from updater import updater, max_id, customer_updater, read_transactions
from admin import Admin
from customer import Customer
from bankaccount import BankAccount
from bankcard import Bankcard

def mainmenu(admins:[Admin], employees:[Employee], customers:[Customer], bankaccounts:[BankAccount], Transaction):
    """
    Főmenü, ez az alapja mindennek, innen indul a bejelentkezés, és kélépés után is ide kerülünk.
    :param admins: lista az összes admin objektummal
    :param employees: lista az összes employee objektummal
    :param customers: lista az összes customer objektummal
    :param bankaccounts: lista az összes bankaccount objektummal
    :param Transaction: Transaction osztály
    :return:
    """
    while True:
        try:
            print(" ")
            print(f"------ Bejelentkezés ------")
            selector = input(
                f"{CYAN}1 - Admin\n2 - Banki alkalmazott\n3 - Ügyfél{RESET}\n{YELLOW}{ITALIC}Válasszon fióktípust a bejelentkezéshez!: {RESET}")
            if selector == "1":
                pid, sid = login(admins)
                adminmenu(pid, sid, admins, employees, customers)
            elif selector == "2":
                pid, sid = login(employees)
                empmenu(pid, sid, employees, customers, bankaccounts, Transaction)
            elif selector == "3":
                pid, sid = login(customers)
                customermenu(pid, sid, customers, bankaccounts, Transaction)
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue

def login(persons):
    """
    Univerzális bejelenkező függvény. Egy objektum tömbből dolgozik és felhasználónév-jelszó segítségével bejelentkezteti az adott típúsú felhasználót.
    :param persons: lista személyekből
    :return: 2db ID: Person ID (pid), Egyedi oszty ID (sid)
    """
    while True:
        print(" ")
        username = input(f"{YELLOW}{ITALIC}Felhasználónév: {RESET}")
        for person in persons:
            if username == person.username:
                sid = int(person.sid)
                pass_validator(person.passwd, persons, sid)
                return int(person.pid), int(person.sid)
        else:
            print(f"{RED}Hibás felhasználónév!{RESET}")
            time.sleep(1)
            continue

def pass_validator(passwd:str, persons, sid):
    """
    Bekér egy jelszót, ellenőrzi, hogy megfelelő-e. 3 próbálkozás után 1 percre letilt.
    :param passwd: felhasználó tényleges jelszava
    :param persons: lista az adott felhasználókból
    :param sid: egyedi felhasználói azonosító
    """
    attempt = 0
    while True:
        if attempt > 2:
            print(f"{RED}3 alkalommal hibás jelszót adott meg. Próbálja újra 1 perc múlva!{RESET}")
            sec = 60
            while sec > 0:
                print(f"{RED}{BOLD}{sec}{RESET}")
                sec -= 1
                time.sleep(1)
            attempt = 0
        inpass = input(f"{YELLOW}{ITALIC}Jelszó: {RESET}")
        if inpass == passwd:
            print(" ")
            print(f"{GREEN}------ Sikeres bejelentkezés! ------{RESET}")
            break
        else:
            print(f"{RED}Hibás jelszó!{RESET}")
            attempt += 1
            time.sleep(1)

def adminmenu(pid:int, sid:int, admins:[Admin], employees:[Employee], customers:[Customer]):
    """
    Admin menü, admin osztály jogosultságaival.
    :param pid: Person ID
    :param sid: Egyedi osztály ID
    :param admins: lista az összes admin objektummal
    :param employees: lista az összes employee objektummal
    :param customers: lista az összes customer objektummal
    """
    while True:
        try:
            print(" ")
            print(f"Admin menü {BOLD}{admins[sid - 1].name}{RESET} részére")
            selector = input(
                f"{CYAN}1 - Új dolgozó létrehozása\n2 - Új admin létrehozása\n3 - Dolgozó adatmódosítás\n4 - Saját adatok módosítása\nx - Kilépés{RESET}\nVálasszon műveletet: ")
            if selector == "1":
                new_emp = Employee(None, None, None, None, None, None, None, None)
                new_emp = Employee.create_person(new_emp)
                employees = employees.append(new_emp)
                employees = updater("Peoples/employees.csv", Employee)
                print(" ")
                print(f"{GREEN}Új dolgozó sikeresen létrehozva {RESET}{BOLD}{CYAN}{new_emp.name}{RESET} {GREEN}néven!{RESET}")
                employees = updater("Peoples/employees.csv", Employee)
                time.sleep(1)
            elif selector == "2":
                new_admin = Admin(None, None, None, None, None, None, None, None)
                new_admin = Admin.create_person(new_admin)
                admins = admins.append(new_admin)
                admins = updater("Peoples/admins.csv", Admin)
                print(" ")
                print(f"{GREEN}Új admin sikeresen létrehozva {RESET}{BOLD}{CYAN}{new_admin.name}{RESET} {GREEN}néven!{RESET}")
                admins = updater("Peoples/admins.csv", Admin)
                time.sleep(1)
            elif selector == "3":
                try:
                    while True:
                        cid = int(input(f"Adja meg a dolgozó ID számát: "))
                        if cid <= max_id(2):
                            Employee.data_updater(employees[cid-1])
                            break
                        else:
                            continue
                except:
                    continue
            elif selector == "4":
                Admin.data_updater(admins[sid-1])
            elif selector == "x":
                break
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue

def empmenu(pid:int, sid:int, employees:[Employee], customers:[Customer], bankaccounts:[BankAccount], Transaction):
    """
    Employee menü, employee osztály jogosultságaival.
    :param pid: Person ID
    :param sid: Egyedi osztály ID
    :param employees: lista az összes employee objektummal
    :param customers: lista az összes customer objektummal
    :param bankaccounts: lista az összes bankszámla objektummal
    :param Transaction: Transaction osztály
    """
    while True:
        try:
            print(" ")
            print(f"Dolgozói menü {BOLD}{employees[sid - 1].name}{RESET} részére")
            selector = input(
                f"{CYAN}1 - Új ügyfél létrehozása\n2 - Ügyfél adatmódosítás\n3 - Ügyfél adat lekérdezés\n4 - Saját adatok módosítása\nx - Kilépés{RESET}\nVálasszon műveletet: ")
            if selector == "1":
                new_customer = Customer(None, None, None, None, None, None, None, None, None)
                new_customer = Customer.create_person(new_customer)
                customers = customers.append(new_customer)
                customers = customer_updater(Customer, BankAccount, Bankcard, Transaction)
                print(" ")
                print(f"{GREEN}Új ügyfél sikeresen létrehozva {RESET}{BOLD}{CYAN}{new_customer.name}{RESET} {GREEN}néven!{RESET}")
                time.sleep(1)

            elif selector == "2":
                try:
                    while True:
                        cid = int(input(f"Adja meg az ügyfél ID számát: "))
                        if cid <= max_id(3):
                            Customer.data_updater(customers[cid-1])
                            break
                        else:
                            continue
                except:
                    continue
            elif selector == "3":
                try:
                    while True:
                        cid = int(input(f"Adja meg az ügyfél ID számát: "))
                        if cid <= max_id(3):
                            print(customers[cid-1])
                            break
                        else:
                            continue
                except:
                    continue
            elif selector == "4":
                Employee.data_updater(employees[sid-1])
            elif selector == "x":
                break
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue

def customermenu(pid:int, sid:int, customers:[Customer], bankaccounts:[BankAccount], Transaction):
    """
    Customer menü, customer osztály jogosultságaival.
    :param pid: Person ID
    :param sid: Egyedi osztály ID
    :param customers: lista az összes customer objektummal
    :param bankaccounts: lista az összes bankszámla objektummal
    :param Transaction: Transaction osztály
    """
    while True:
        try:
            print(" ")
            print(f"Ügyfél menü {BOLD}{customers[sid - 1].name}{RESET} részére")
            selector = input(
                f"{CYAN}1 - Banki átutalás\n2 - Saját adatok megtekintése\n3 - Tranzakciók listázása\nx - Kilépés{RESET}\nVálasszon műveletet: ")
            if selector == "1":
                while True:
                    tsid = int(input(f"{YELLOW}{ITALIC}Adja meg a kedvezményezett ID számát: {RESET}"))
                    if tsid == sid:
                        print(f"{RED}Hiba! Saját számlára nem lehet utalni!{RESET}")
                        continue
                    elif tsid <= max_id(3):
                        while True:
                            amount = int(input(f"{YELLOW}{ITALIC}Adja meg az utalni kívánt összeget: {RESET}"))
                            if amount > int(bankaccounts[sid-1].balance):
                                print(f"{RED}Nincs elegendő fedezet a számlán! Hiányzik: {amount-int(bankaccounts[sid-1].balance)}{RESET}")
                                break
                            else:
                                Customer.transfer(customers[sid-1], sid, tsid, amount, bankaccounts)
                                customers = customer_updater(Customer, BankAccount, Bankcard)
                                break
                        break
                    else:
                        print(f"{RED}Nem létező ID szám!{RESET}")
                        time.sleep(1)
                        continue

            elif selector == "2":
                print(customers[sid-1])
            elif selector == "3":
                transactions = read_transactions(Transaction, BankAccount)
                trs = transactions[sid-1]
                for tr in trs:
                    print(tr)
            elif selector == "x":
                break
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue