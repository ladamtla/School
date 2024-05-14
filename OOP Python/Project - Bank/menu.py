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
            print(f"{BGYELLOW}{BLACK}------ Login ------{RESET}")
            selector = input(
                f"{CYAN}1 - Admin\n2 - Employee\n3 - Customer{RESET}\n{YELLOW}{ITALIC}Choose an account type to login with!: {RESET}")
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
                print(f"{RED}Wrong menu option!{RESET}")
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
        username = input(f"{YELLOW}{ITALIC}Username: {RESET}")
        for person in persons:
            if username == person.username:
                sid = int(person.sid)
                pass_validator(person.passwd, persons, sid)
                return int(person.pid), int(person.sid)
        else:
            print(f"{RED}Wrong username!{RESET}")
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
            print(f"{RED}You have entered an incorrect password 3 times. Try again in 1 minute!{RESET}")
            sec = 60
            while sec > 0:
                print(f"{RED}{BOLD}{sec}{RESET}")
                sec -= 1
                time.sleep(1)
            attempt = 0
        inpass = input(f"{YELLOW}{ITALIC}Password: {RESET}")
        if inpass == passwd:
            print(" ")
            print(f"{GREEN}------ Successful Login! ------{RESET}")
            break
        else:
            print(f"{RED}Wrong password!{RESET}")
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
            print(f"Admin menu for {BOLD}{admins[sid - 1].name}{RESET} ")
            selector = input(
                f"{CYAN}1 - Add new employee\n2 - Add new admin\n3 - Modify employee data\n4 - Modify own data\nx - Exit{RESET}\n{YELLOW}{ITALIC}Choose an option: {RESET}")
            if selector == "1":
                new_emp = Employee(None, None, None, None, None, None, None, None)
                new_emp = Employee.create_person(new_emp)
                employees = employees.append(new_emp)
                employees = updater("People/employees.csv", Employee)
                print(" ")
                print(f"{GREEN}New employee created: {RESET}{BOLD}{CYAN}{new_emp.name}{RESET}")
                employees = updater("People/employees.csv", Employee)
                time.sleep(1)
            elif selector == "2":
                new_admin = Admin(None, None, None, None, None, None, None, None)
                new_admin = Admin.create_person(new_admin)
                admins = admins.append(new_admin)
                admins = updater("People/admins.csv", Admin)
                print(" ")
                print(f"{GREEN}New admin created: {RESET}{BOLD}{CYAN}{new_admin.name}{RESET} ")
                admins = updater("People/admins.csv", Admin)
                time.sleep(1)
            elif selector == "3":
                try:
                    while True:
                        cid = int(input(f"{YELLOW}{ITALIC}Enter the employee ID number: {RESET}"))
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
                print(f"{RED}Wrong menu option!{RESET}")
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
            print(f"Employee menu for {BOLD}{employees[sid - 1].name}{RESET}")
            selector = input(
                f"{CYAN}1 - Add new customer\n2 - Modify employee data\n3 - Retrieve customer data\n4 - Modify own data\nx - Exit{RESET}\n{YELLOW}Choose an option: {RESET}")
            if selector == "1":
                new_customer = Customer(None, None, None, None, None, None, None, None, None)
                new_customer = Customer.create_person(new_customer)
                customers = customers.append(new_customer)
                customers = customer_updater(Customer, BankAccount, Bankcard, Transaction)
                print(" ")
                print(f"{GREEN}New customer created: {RESET}{BOLD}{CYAN}{new_customer.name}{RESET}")
                time.sleep(1)

            elif selector == "2":
                try:
                    while True:
                        cid = int(input(f"{YELLOW}{ITALIC}Enter customer ID number: {RESET}"))
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
                        cid = int(input(f"{YELLOW}{ITALIC}Enter customer ID number: {RESET}"))
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
                print(f"{RED}Wrong menu option!{RESET}")
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
            print(f"Customer menu for {BOLD}{customers[sid - 1].name}{RESET}")
            selector = input(
                f"{CYAN}1 - Bank transfer\n2 - Check own data\n3 - List of transactions\nx - Exit{RESET}\n{ITALIC}{YELLOW}Choose an option: {RESET}")
            if selector == "1":
                while True:
                    tsid = int(input(f"{YELLOW}{ITALIC}Enter the recipient ID number: {RESET}"))
                    if tsid == sid:
                        print(f"{RED}Error! You cannot transfer to your own account!{RESET}")
                        continue
                    elif tsid <= max_id(3):
                        while True:
                            amount = int(input(f"{YELLOW}{ITALIC}Enter the amount you want to transfer: {RESET}"))
                            if amount > int(bankaccounts[sid-1].balance):
                                print(f"{RED}Not enough funds in the account! Missing: {amount-int(bankaccounts[sid-1].balance)}{RESET}")
                                break
                            else:
                                Customer.transfer(customers[sid-1], sid, tsid, amount, bankaccounts)
                                customers = customer_updater(Customer, BankAccount, Bankcard)
                                break
                        break
                    else:
                        print(f"{RED}Non-existent ID number!{RESET}")
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
                print(f"{RED}Wrong menu option!{RESET}")
                time.sleep(1)
        except:
            continue