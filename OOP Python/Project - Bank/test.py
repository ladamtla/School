from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater, customer_updater, read_transactions
from menu import mainmenu
import time
from format import *
from bankaccount import BankAccount
from bankcard import Bankcard
from transaction import Transaction

tr = read_transactions(Transaction, BankAccount)
print(tr)