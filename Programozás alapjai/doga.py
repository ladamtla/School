import random

def randomPointGenerator(stop):
    tests = []
    for i in range(0, 10):
        i = random.randint(0, stop)
        tests.append(i)
    return tests

def Best4Point(points, maxpoint):
    bfp = 0
    list = []
    for i in points:
        if i == 0:
            pass
        else:
            if i/maxpoint >= 0.78 and i/maxpoint <= 0.84:
                list.append(i)
    bfp = 0
    for i in list:
        if i > bfp:
            bfp = i
    return bfp


while True:
    try:
        maxpoint = int(input("Pontszám tartomány felső határa: "))
    except:
        print("Beolvasási hiba, kérlek egy pozitív egész számot adj meg!")
    else:
        if maxpoint > 30 and maxpoint < 50:
            points = randomPointGenerator(maxpoint)

            print(f"Pontszámok: {points}")
            if Best4Point(points, maxpoint) == 0:
                print("A pontszámok alapján nincsen 4-es dolgozat")
            else:
                print(f"A legjobb 4-es dolgozat pontszáma: {Best4Point(points, maxpoint)}")
            break
        else:
            print("Beolvasási hiba, kérlek egy 30 és 50 közé eső egész számot adj meg!")