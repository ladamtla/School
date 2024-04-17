from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater
from bankaccount import BankAccount
from bankcard import Bankcard


admins = updater("Peoples/admins.csv", Admin)
employees = updater("Peoples/employees.csv", Employee)
customers = updater("Peoples/customers.csv", Customer)
#ba = BankAccount("11111111-11111111-11111111", 1000000, [], [])
#bc = Bankcard(1234567891234567, "04/29", 985, "visa", 1234567854541254)

bc = Bankcard.user_select_card()

#customers[2].data_updater()
#print(customers[2])
print(bc)