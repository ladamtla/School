i = 0

while True:
    be = input("Írj be egy számot: ")
    if be == "x":
        print(f"Program vége. Összesen {i} művelet történt")
        break
    else:
        szam = int(be)
        if szam % 2 == 0:
            print("Ez a szám páros")
            i += 1
        else:
            print("Ez a szám páratlan")
            i += 1