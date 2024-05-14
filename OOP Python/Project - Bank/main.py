#Szükséges fájlok, metódusok és függvények importálása
from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater, customer_updater
from menu import mainmenu
from bankaccount import BankAccount
from bankcard import Bankcard
from transaction import Transaction

#Adatok frissításe, objektumok látrehozása
bankaccounts = updater("data/bankaccounts.csv", BankAccount)
customers = customer_updater(Customer, BankAccount, Bankcard, Transaction)
admins = updater("People/admins.csv", Admin)
employees = updater("People/employees.csv", Employee)

#Rendszer elindítása
mainmenu(admins, employees, customers, bankaccounts, Transaction)
