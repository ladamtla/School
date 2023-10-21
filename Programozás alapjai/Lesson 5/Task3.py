# Definiáljuk a függvényt
def is_prime(number):

    # Az 1 nem prímszám
    if number == 1:
        return False

    # A szám gyöke+1 -ig vizsgáljuk a számokat
    for i in range(2, int(number**0.5) + 1):

        # Ha találunk oylan számot amivel osztható akkor nem prímszám
        if number % i == 0:
            return False

    # Ha nem találunk akkor prímszám
    return True

# Ellenőrzött bemeneten bekérünk egy számot
while True:
    x = int(input("Adj meg egy számot: "))
    if x > 0:
        break
    else:
        print("Error")

# Kiírjuk a meghívott függvényt
print(is_prime(x))


