# Egy listában eltároljuk a hívások kötségeit, definiáljuk a válltozókat
types = [40, 60, 100]
ty = 0
szum = 0

# Üres sztring bemenet esetén megszakitja a ciklust
# Ellenkező esetben először bekéri a hívás típusát, majd a beszélgetés idejét
# Ezt a két adatot felhasználva kiszámítja a hívás költségét, amit hozzáad az összeg válltozóhoz, majd kéri a következő hívás típusát
while True:
    ty = input("Add meg a hívás típusát(1,2,3): ")
    if ty == "":
        break
    else:
        ty = int(ty)
        time = int(input("Add meg a beszélgetés idejét: "))
        szum = szum + (time*types[ty-1])

# Kiírjuk az eredményt
print(f"Költség: {szum} Ft")