import csv

from format import *
def updater(filename, clas):
    list = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            i = clas(*row)
            list.append(i)
    return list

def read_customers(filename, Customer):
    customers = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            customer = Customer(row[0], int(row[1]), row[2], row[3], row[4], row[5], int(row[6]), int(row[7]), None)
            customers.append(customer)
    return customers

def read_bankaccounts(filename, BankAccount):
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

    return list

def customer_updater(Customer, BankAccount):
    customers = read_customers("Peoples/customers.csv", Customer)
    bankaccounts = read_bankaccounts("bankaccounts.csv", BankAccount)
    link_bankaccounts_to_customers(customers, bankaccounts)
    return customers

def csv_writer(file_path, search_key, new_data):
    # Olvasd be a meglévő adatokat a CSV fájlból
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Keresd meg a sorokat, amelyeket frissíteni kell
    for row in data:
        if row[6] == search_key:  # Feltételezzük, hogy az 7. oszlop a kulcs
            for i in range(len(row)):
                if new_data[i] is not None:  # Ha az új adat nem None
                    row[i] = new_data[i]  # Frissítsd az adatot

    # Írd felül az összes sort a frissített adatokkal
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def max_id(num):

    adminids = []
    empids = []
    customerids = []
    pids1 = []
    pids2 = []
    pids3 = []

    with open("Peoples/admins.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                adminids.append(int(row[7]))
                pids1.append(int(row[6]))
            except ValueError:
                pass

    with open("Peoples/employees.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                empids.append(int(row[7]))
                pids2.append(int(row[6]))
            except ValueError:
                pass

    with open("Peoples/customers.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                customerids.append(int(row[7]))
                pids3.append(int(row[6]))
            except ValueError:
                pass

    pids = pids1 + pids2 + pids3
    maxadminid = max(adminids)
    maxempid = max(empids)
    maxcustomerid = max(customerids)
    maxpid = max(pids)

    if num == 0:
        return maxpid
    elif num == 1:
        return maxadminid
    elif num == 2:
        return maxempid
    elif num == 3:
        return maxcustomerid

def max_baid():

    baids = []
    with open("bankaccounts.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                baids.append(int(row[4]))
            except ValueError:
                pass
    maxbaid = max(baids)
    return maxbaid
