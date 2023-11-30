"""
Lénárt Ádám Tamás - YYBBFJ
"""


import random


def randomPointGenerator(stop):
    tests = []
    for i in range(0, 10):
        i = random.randint(0, stop)
        tests.append(i)

    return tests
def fiveCounter(points, maxpoint):
    counter = 0
    for i in points:
        if i == 0:
            pass
        else:
            if i / maxpoint >= 0.8:
                counter += 1
    return counter

while True:
    try:
        maxpoint = int(input("Pontszám tartomány felső határa: "))
    except:
        print("Beolvasási hiba, kérlek egy pozitív egész számot adj meg!")
    else:
        if maxpoint > 30 and maxpoint < 50:
            points = randomPointGenerator(maxpoint)
            print(f"Pontszámok: {points}")
            print(f"Összesen {fiveCounter(points, maxpoint)}db ötös dolgozat van.")
            break
        else:
            print("Beolvasási hiba, kérlek egy 30 és 50 közé eső egész számot adj meg!")









