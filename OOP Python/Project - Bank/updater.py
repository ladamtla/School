import csv



def updater(filename:str, clas):
    """
    Univerzális updater függvény, objektum listát hoz létre csv fájlból
    :param filename: fájlnév szövegként
    :param clas: objektumok osztálya
    :return: objektum lista
    """
    list = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            i = clas(*row)
            list.append(i)
    return list


def read_customers(filename:str, Customer):
    """
    Specifikusan ügyfeleket olvas be egy fájból, objektum listát hoz létre
    :param filename: csv fájlneve
    :param Customer: Customer osztály
    :return: lista a létrehozott Customer objektumokkal
    """
    customers = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            customer = Customer(row[0], int(row[1]), row[2], row[3], row[4], row[5], int(row[6]), int(row[7]), None)
            customers.append(customer)
    return customers

def read_bankaccounts(filename:str, BankAccount):
    """
    Specifikusan bankszámlákat olvas be egy fájból, objektum listát hoz létre
    :param filename: csv fájlneve
    :param BankAccount: BankAccount osztály
    :return: lista a létrehozott BankAccount objektumokkal
    """
    bankaccounts = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            bankaccount = BankAccount(row[0], int(row[1]), int(row[2]), [], int(row[4]))
            bankaccounts.append(bankaccount)
    return bankaccounts

def read_transactions(Transaction, BankAccount):
    """
    Specifikusan tranzakciókat olvas be egy fájból, objektum listák listáját hozza létre
    :param Transaction: Transaction osztály
    :param BankAccount: BankAccount osztály
    :return: egy lista mely sorban ügyfelenként listákat tartalmaz, a belső listák az adott ügyfél tranzakcióit tartalmazza Transaction objektumokként
    """
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
    """
    Hozzárendeli a tranzakció lista objektumokat a bankszámlákhoz
    :param transactions: tranzakció objektumokat tartalmazó listák listája
    :param bankaccounts: BankAccount típusú objektumokat tartalmazó lista
    """
    trcl = 0
    for bankaccount in bankaccounts:
        bankaccount.transactions = transactions[0]
        trcl += 1

def link_bankaccounts_to_customers(customers, bankaccounts):
    """
    Hozzárendeli az ügyfelekhez a bankszámláikat.
    :param customers: Customer objektumokat tartalmazó lista
    :param bankaccounts: BankAccount objektumokat tartalmazó lista
    :return:
    """
    for customer in customers:
        for bankaccount in bankaccounts:
            if customer._Customer__sid == bankaccount._BankAccount__baid:
                customer._Customer__bankaccount = bankaccount
                break

    return list

def read_bankcards(filename:str, Bankcard):
    """
    Specifikusan bakkártyákat olvas be egy fájból, objektum listák listáját hozza létre
    :param filename: fájl neve szövegként
    :param Bankcard: Bankcard osztály
    :return: Bankcard objektumokat tartalmazó lista
    """
    bankcards = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            customer = Bankcard(int(row[0]), row[1], int(row[2]), row[3], int(row[4]))
            bankcards.append(customer)
    return bankcards

def link_bankcards_to_bankaccount(bankcards, bankaccounts):
    """
    Hozzárendeli a bankkártyákat a bankszámlákhoz,
    :param bankcards: Bankcard objektumokat tartalmazó lista
    :param bankaccounts: BankAccount objektumokat tartalmazó lista
    :return: új, bővített BankAccount objektumokat tartalmazó lista
    """
    for bankaccount in bankaccounts:
        for bankcard in bankcards:
            if bankaccount.bankcard == bankcard.cardnum:
                bankaccount.bankcard = bankcard
                break

    return bankaccounts

def customer_updater(Customer, BankAccount, Bankcard, Transaction):
    """
    Több függvény együttes, összehangolt futtatásával frissíti az ügyfél objaktumokat tartalmazó listát
    :param Customer: Customer osztály
    :param BankAccount: BankAccount osztály
    :param Bankcard: Bankcard osztály
    :param Transaction: Transaction osztály
    :return: frissített Customer objektumokat tartalmatzó lista
    """
    transactions = read_transactions(Transaction, BankAccount)
    customers = read_customers("Peoples/customers.csv", Customer)
    bankaccounts = read_bankaccounts("bankaccounts.csv", BankAccount)
    bankcards = read_bankcards("bankcards.csv", Bankcard)
    link_transactions_to_bankaccount(transactions, bankaccounts)
    link_bankcards_to_bankaccount(bankcards, bankaccounts)
    link_bankaccounts_to_customers(customers, bankaccounts)
    return customers

def csv_writer(file_path, search_key, new_data):
    """
    Egy lista alapján frissíti a csv fájl adatait.
    :param file_path: csv fájl név szövegként
    :param search_key: keresési kulcs (a 7. oszlopban szerepeljen!)
    :param new_data: új adatok listában (ami nem frissül oda "None")
    """
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    for row in data:
        if int(row[6]) == int(search_key):
            for i in range(len(row)):
                if new_data[i] is not None:
                    row[i] = new_data[i]

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def max_id(num:int)->int:
    """
    Új felhasználók létrehozásánál az új ID generálásához használatos egéd függvény amely típusonként és egyben is öszeszámolja, és visszaadja a legmagasabb jelenlegi id számot.
    :param num: 0 esetén: Max Person ID értéke (pid),
                1 esetén: Max Admin ID értéke (sid),
                2 esetén: Max Employee ID értéke (sid),
                3 esetén: Max Customer ID értéke (sid)
    :return: adott maximálsi id
    """

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

def max_baid()->int:
    """
    Maximális bankszámla ID számát adja vissza
    :return: Max baID
    """

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

def max_trid(sid:int)->int:
    """
    Egy adott ügyfélhez tartózó maximális tranzakció id számát adja vissza
    :param sid: ügyfél id száma
    :return: max tarzakció id
    """

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

def csv_writer_balance(sid:int, new_balance:int):
    """
    Egyenleg frissítő, id és új egyenleg alapján
    :param sid: ügyfél id száma
    :param new_balance: új egyenleg
    """

    with open("bankaccounts.csv", 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    for row in data:
        if row[-1] == str(sid):
            row[1] = str(new_balance)

    with open("bankaccounts.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)





