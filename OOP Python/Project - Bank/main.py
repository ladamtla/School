from admin import Admin
from employee import Employee
from customer import Customer
from updater import updater


admins = updater("Peoples/admins.csv", Admin)
employees = updater("Peoples/employees.csv", Employee)
customers = updater("Peoples/customers.csv", Customer)

print(customers[2])