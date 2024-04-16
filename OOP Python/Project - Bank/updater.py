import csv
from admin import Admin
from employee import Employee
from customer import Customer

def updater(filename, clas):
    list = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            admin = clas(*row)
            list.append(admin)
    return list



