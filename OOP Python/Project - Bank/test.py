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

sid = 5
transactions = read_transactions(Transaction, BankAccount)
trs = transactions[sid-1]
print(transactions)
print(trs)

