from format import *
import time

def login(admins, employees, customers):
    while True:
        try:
            selector = input(
                f"{CYAN}1 - Admin\n2 - Banki alkalmazott\n3 - Felhasználó{RESET}\nVálasszon fióktípust a bejelentkezéshez!: ")
            if selector == "1":
                adminlogin(admins)
                break
            elif selector == "2":
                emplogin(employees)
                break
            elif selector == "3":
                customerlogin(customers)
                break
            else:
                print(f"{RED}Hibás menüpont!{RESET}")
                time.sleep(1)
        except:
            continue

def username_validator(admins, username):
    for admin in admins:
        if admin.username == username:
            print("Felhasználónév megtalálva!")
            return True, admin.passw  # Return True and the corresponding password
    print("Nem található ilyen felhasználónév!")
    return False, None

def adminlogin(admins):
    attempts = 0
    while attempts < 3:
        try:
            username = input(f"{BLUE}Felhasználónév: ")
            valid, passwd = username_validator(admins, username)
            if valid == True:
                print(f"Létező felhasználónév!")
                break
            else:
                print(f"{RED}Nem létező felhsználónév!{RESET}")
                time.sleep(1)
        except:
            continue

