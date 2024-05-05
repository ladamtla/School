import csv

def full_updater(Bankcard, BankAccount, Admin, Customer, Employee, Transaction):
    bankcards = updater("bankcards.csv", Bankcard)
    bankaccounts = updater("bankaccounts.csv", BankAccount)
    customers = customer_updater(Customer, BankAccount, Bankcard, Transaction)
    admins = updater("Peoples/admins.csv", Admin)
    employees = updater("Peoples/employees.csv", Employee)

    return bankcards, bankaccounts, customers, admins, employees
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
            bankaccount = BankAccount(row[0], int(row[1]), int(row[2]), [], int(row[4]))
            bankaccounts.append(bankaccount)
    return bankaccounts

def read_transactions(Transaction, BankAccount):
    transactions = []
    bankaccounts = read_bankaccounts("bankaccounts.csv", BankAccount)
    for bankaccount in bankaccounts:
        transactionsparts = []
        with open(f"Transactiondata/{bankaccount.baid}.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                transactionspart = Transaction(int(row[0]), row[1], row[2], int(row[3]), row[4])
                transactionsparts.append(transactionspart)
                transactions.append(transactionsparts)
    return transactions

def link_transactions_to_bankaccount(transactions, bankaccounts):
    trcl = 0
    for bankaccount in bankaccounts:
        bankaccount.transactions = transactions[0]
        trcl += 1


def link_bankaccounts_to_customers(customers, bankaccounts):
    for customer in customers:
        for bankaccount in bankaccounts:
            if customer._Customer__sid == bankaccount._BankAccount__baid:
                customer._Customer__bankaccount = bankaccount
                break

    return list

def read_bankcards(filename, Bankcard):
    bankcards = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            customer = Bankcard(int(row[0]), row[1], int(row[2]), row[3], int(row[4]))
            bankcards.append(customer)
    return bankcards

def link_bankcards_to_bankaccount(bankcards, bankaccounts):
    for bankaccount in bankaccounts:
        for bankcard in bankcards:
            if bankaccount.bankcard == bankcard.cardnum:
                bankaccount.bankcard = bankcard
                break

    return bankaccounts

def customer_updater(Customer, BankAccount, Bankcard, Transaction):
    transactions = read_transactions(Transaction, BankAccount)
    customers = read_customers("Peoples/customers.csv", Customer)
    bankaccounts = read_bankaccounts("bankaccounts.csv", BankAccount)
    bankcards = read_bankcards("bankcards.csv", Bankcard)
    link_transactions_to_bankaccount(transactions, bankaccounts)
    link_bankcards_to_bankaccount(bankcards, bankaccounts)
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

def max_trid(sid):

    sid = int(sid)
    filename = f"Transactiondata/{sid}.csv"
    trids = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                trids.append(int(row[0]))
            except ValueError:
                pass
    trid = max(trids)
    return trid

def csv_writer_balance(id_number, new_balance):
    # Olvasd be a CSV fájlt
    with open("bankaccounts.csv", 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Keresd meg a sorokat, amelyekben az id_number megegyezik
    for row in data:
        if row[-1] == str(id_number):  # Az utolsó oszlop tartalmazza az ID-t
            row[1] = str(new_balance)  # A balance az 2. oszlop

    # Írd felül a fájlt az új adatokkal
    with open("bankaccounts.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)





