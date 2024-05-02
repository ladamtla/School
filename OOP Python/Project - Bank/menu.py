from format import *
import time
from employee import Employee
from updater import updater, max_id
from admin import Admin
from customer import Customer
from bankaccount import BankAccount

def mainmenu(admins, employees, customers, bankaccounts):
    while True:
        try:
            print(" ")
            print(f"------ Bejelentkezés ------")
            selector = input(
                f"{CYAN}1 - Admin\n2 - Banki alkalmazott\n3 - Felhasználó{RESET}\nVálasszon fióktípust a bejelentkezéshez!: ")
            if selector == "1":
                pid, sid = login(admins)
                adminmenu(pid, sid, admins, employees, customers)
            elif selector == "2":
                pid, sid = login(employees)
                empmenu(pid, sid, employees, customers, bankaccounts)
            elif selector == "3":
                pid, sid = login(customers)
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue
    return pid, selector

def login(persons):
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
            continue



def pass_validator(passwd, persons, sid):
    while True:
        inpass = input(f"{YELLOW}{ITALIC}Jelszó: {RESET}")
        if inpass == passwd:
            print(" ")
            print(f"{GREEN}------ Sikeres bejelentkezés! ------{RESET}")
            break
        else:
            print(f"{RED}Hibás jelszó!{RESET}")




def adminmenu(pid, sid, admins, employees, customers):

    while True:
        try:
            print(" ")
            print(f"Admin menü {BOLD}{admins[sid - 1].name}{RESET} részére")
            selector = input(
                f"{CYAN}1 - Új dolgozó létrehozása\n2 - Új admin létrehozása\n3 - Dolgozó adatmódosítás\n4 - Saját adatok módosítása\nx - Kilépés{RESET}\nVálasszon műveletet: ")
            if selector == "1":
                new_emp = Employee(None, None, None, None, None, None, None, None)
                new_emp = Employee.create_person(new_emp)
                employees = updater("Peoples/employees.csv", Employee)
                print(" ")
                print(f"{GREEN}Új dolgozó sikeresen létrehozva {RESET}{BOLD}{CYAN}{new_emp.name}{RESET} {GREEN}néven!{RESET}")
            elif selector == "2":
                new_admin = Admin(None, None, None, None, None, None, None, None)
                new_admin = Admin.create_person(new_admin)
                admins = updater("Peoples/admins.csv", Admin)
                print(" ")
                print(f"{GREEN}Új admin sikeresen létrehozva {RESET}{BOLD}{CYAN}{new_admin.name}{RESET} {GREEN}néven!{RESET}")
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

def empmenu(pid, sid, employees, customers, bankaccounts):

    while True:
        try:
            print(" ")
            print(f"Dolgozói menü {BOLD}{employees[sid - 1].name}{RESET} részére")
            selector = input(
                f"{CYAN}1 - Új ügyfél létrehozása\n2 - Új bankszámla létrehozása\n3 - Ügyfél adatmódosítás\n4 - Saját adatok módosítása\nx - Kilépés{RESET}\nVálasszon műveletet: ")
            if selector == "1":
                new_customer = Customer(None, None, None, None, None, None, None, None, None)
                new_customer = Customer.create_person(new_customer)
                customers = updater("Peoples/customers.csv", Customer)
                print(" ")
                print(f"{GREEN}Új ügyfél sikeresen létrehozva {RESET}{BOLD}{CYAN}{new_customer.name}{RESET} {GREEN}néven!{RESET}")
            elif selector == "2":
                try:
                    while True:
                        cid = int(input(f"Adja meg az ügyfél ID számát aki számára a bankszámlát szeretne létrehozni: "))
                        print("111")
                        if cid <= max_id(3):
                            print("222")
                            new_ba = BankAccount(None, None, None, None, None)
                            print("333")
                            new_ba = BankAccount.create_ba(new_ba)
                            print("444")
                            bankaccounts = updater("bankaccounts.csv", BankAccount)
                            print(f"cid: {cid}")
                            Customer.ba_append(customers[cid-1], new_ba)
                            customers = updater("Peoples/customers.csv", Customer)
                            print("666")
                            print(" ")
                            print(f"{GREEN}Új bankszámla sikeresen létrehozva!{RESET}")
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
                            Customer.data_updater(customers[cid-1])
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


