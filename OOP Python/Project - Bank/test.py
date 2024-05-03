from customer import Customer
from updater import updater, link_bankaccounts_to_customers
from admin import Admin
from employee import Employee
from bankaccount import BankAccount
import csv


#bankaccounts = updater("bankaccounts.csv", BankAccount)
#customers = updater("Peoples/customers.csv", Customer)
#link_bankaccounts_to_customers(customers, bankaccounts)
#admins = updater("Peoples/admins.csv", Admin)
#employees = updater("Peoples/employees.csv", Employee)

c

def read_bankaccounts(filename):
    bankaccounts = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            bankaccount = BankAccount(row[0], int(row[1]), [], [], int(row[4]))
            bankaccounts.append(bankaccount)
    return bankaccounts

def link_bankaccounts_to_customers(customers, bankaccounts):
    for customer in customers:
        for bankaccount in bankaccounts:
            if customer._Customer__sid == bankaccount._BankAccount__baid:
                customer._Customer__bankaccount = bankaccount
                break

def customer_updater(customers_filename, bankaccounts_filename):
    customers = read_customers("Peoples/customers.csv")
    bankaccounts = read_bankaccounts("bankaccounts.csv")
    link_bankaccounts_to_customers(customers, bankaccounts)
    return customers

# Teszt
customers = customer_updater("Peoples/customers.csv", "bankaccounts.csv")
for customer in customers:
    print(customer._Person__name, customer._Customer__bankaccount._BankAccount__accountnum)

