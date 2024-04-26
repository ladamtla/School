from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater
from format import *
from bankaccount import BankAccount
from bankcard import Bankcard


admins = updater("Peoples/admins.csv", Admin)
employees = updater("Peoples/employees.csv", Employee)
customers = updater("Peoples/customers.csv", Customer)
#bc = Bankcard(None, None, None, None, None)


#bc = Bankcard.create_bankcard(Bankcard, "bc1")
#print(bc)

customers[4].data_updater()
print(customers[4])

#print(customers[0])
