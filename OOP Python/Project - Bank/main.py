from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater, link_bankaccounts_to_customers, customer_updater
from menu import mainmenu
import time
from format import *
from bankaccount import BankAccount
from bankcard import Bankcard

bankaccounts = updater("bankaccounts.csv", BankAccount)
customers = customer_updater(Customer, BankAccount)
admins = updater("Peoples/admins.csv", Admin)
employees = updater("Peoples/employees.csv", Employee)

print(customers[0])
print(bankaccounts[0])

mainmenu(admins, employees, customers, bankaccounts)
