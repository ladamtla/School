valaszto = "y"

while True:
    if valaszto == "y":
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
        if muvelet == "+":
            print(f"{szam1} + {szam2} = {szam1 + szam2}")
        if muvelet == "-":
            print(f"{szam1} - {szam2} = {szam1 - szam2}")
        if muvelet == "*":
            print(f"{szam1} * {szam2} = {szam1 * szam2}")
        if muvelet == "/":
            print(f"{szam1} / {szam2} = {szam1 / szam2}")
        while True:
            valaszto = input("Szeretnél tovább számolni? (y/n): ")
            if valaszto == "y":
                break
            elif valaszto == "n":
                break
            else:
                print("Hiba")
                continue
    else:
        break