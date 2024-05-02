from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater
from menu import login, mainmenu
import time
from format import *
from bankaccount import BankAccount
from bankcard import Bankcard


admins = updater("Peoples/admins.csv", Admin)
employees = updater("Peoples/employees.csv", Employee)
customers = updater("Peoples/customers.csv", Customer)
bankaccounts = updater("bankaccounts.csv", BankAccount)

mainmenu(admins, employees, customers, bankaccounts)
