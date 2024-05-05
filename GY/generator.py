import csv
import random

def create_random_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(1, 1001):
            num1 = ''.join(random.choices('0123456789', k=12))  # 12 random szám
            num2 = ''.join(random.choices('0123456789', k=18))  # 18 random szám
            y = i
            writer.writerow([f'221024{num1}', '0', f'{num2}', '[]', y])

# Tesztelés
create_random_csv('random_data.csv')
