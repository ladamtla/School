# Definiálunk egy segédválltozót az továbbszámolás ellenőrzéséhez
valaszto = "y"

# Amíg a valaszto értéke "y", elindítjuk a számolási folyamatot, ha "n" akkor leáll a program
while valaszto == "y":

    # Bekérjük a 2 számot, majd a műveleti jelet
    szam1 = int(input("Írja be az első számot: "))
    szam2 = int(input("Írja be az második számot: "))
    while True:
        muvelet = input("Írjon be gy műveleti jelet (+; -; *; /): ")
        if muvelet == "+":
            break
        elif muvelet == "-":
            break
        elif muvelet == "*":
            break
        elif muvelet == "/":
            break
        else:
            continue

    # A műveleti jel alapján kiszámoljuk az eredményt, kiírjuk, figyelve a 0-val való osztási hibára
    if muvelet == "+":
        print(f"{szam1} + {szam2} = {szam1 + szam2}")
    if muvelet == "-":
        print(f"{szam1} - {szam2} = {szam1 - szam2}")
    if muvelet == "*":
        print(f"{szam1} * {szam2} = {szam1 * szam2}")
    if muvelet == "/":
        if szam2 == 0:
            print("0-val nem lehet osztani!")
        else:
            print(f"{szam1} / {szam2} = {szam1 / szam2}")

    # Megkérdezzük, hogy szeretne-e tovább számolni, ha igen akkor kezdődik előröl, ha nem akkor leáll a program
    while True:
        valaszto = input("Szeretnél tovább számolni? (y/n): ")
        if valaszto == "y":
            break
        elif valaszto == "n":
            break
        else:
            print("Hiba")
            continue