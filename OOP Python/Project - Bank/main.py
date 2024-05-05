from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater, customer_updater, full_updater
from menu import mainmenu
import time
from format import *
from bankaccount import BankAccount
from bankcard import Bankcard
from transaction import Transaction


bankaccounts = updater("bankaccounts.csv", BankAccount)
customers = customer_updater(Customer, BankAccount, Bankcard, Transaction)
admins = updater("Peoples/admins.csv", Admin)
employees = updater("Peoples/employees.csv", Employee)


mainmenu(admins, employees, customers, bankaccounts, Transaction)
