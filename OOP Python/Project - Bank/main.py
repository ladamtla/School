from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater
from menu import mainmenu
import time
from format import *
from bankaccount import BankAccount
from bankcard import Bankcard


admins = updater("Peoples/admins.csv", Admin)
employees = updater("Peoples/employees.csv", Employee)
customers = updater("Peoples/customers.csv", Customer)
bankaccounts = updater("bankaccounts.csv", BankAccount)
#bc = Bankcard(None, None, None, None, None)


#bc = Bankcard.create_bankcard(Bankcard, "bc1")
#print(bc)

#new_cust = Customer(None, None, None, None, None, None, None, None, None)
#new_emp = Customer.create_person(new_cust)

#update_admin = Admin.data_updater(admins[0])

#print(customers[6])

#mainmenu(admins, employees, customers, bankaccounts)

ba = BankAccount(None, None, None, None, None)
BankAccount.create_ba(ba)
print(ba)
