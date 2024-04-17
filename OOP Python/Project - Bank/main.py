from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater
from bankaccount import BankAccount


admins = updater("Peoples/admins.csv", Admin)
employees = updater("Peoples/employees.csv", Employee)
customers = updater("Peoples/customers.csv", Customer)
#ba = BankAccount("11111111-11111111-11111111", 1000000, [], [])



customers[2].data_updater()
print(employees[2])