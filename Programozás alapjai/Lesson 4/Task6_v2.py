# Definiálunk egy segédválltozót az továbbszámolás ellenőrzéséhez
valaszto = "y"

# Amíg a valaszto értéke "y", elindítjuk a számolási folyamatot, ha "n" akkor leáll a program
while valaszto == "y":

    # Bekérünk egy sztringet, amit szétválasztunk válltozókba, majd számmá konvertáljuk a 2 számot
    bemenet = input("Add meg a műveletet az alábbi minta alapján: '1 + 2': ")
    szam1, muvelet, szam2 = bemenet.split(sep=" ")
    szam1 = int(szam1)
    szam2 = int(szam2)

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