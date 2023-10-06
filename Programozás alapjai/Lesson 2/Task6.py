# Bekérünk egy számot
num = int(input("Adj meg egy számot: "))

# Egy elágazással megvizsgáljuk, hogy a szám kettőfel osztva 0, vagy 1 maradékot ad
# majd ezek alapján kiíratjuk a konzolra az eredményt
if num % 2 == 0:
    print(f"A(z) '{num}' páros")
else:
    print(f"A(z) '{num}' páratlan")