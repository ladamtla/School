types = [40, 60, 100]
ty = 0
szum = 0

while True:
    ty = input("Add meg a hívás típusát(1,2,3): ")
    if ty == "":
        break
    else:
        ty = int(ty)
        time = int(input("Add meg a beszélgetés idejét: "))
        szum = szum + (time*types[ty-1])

print(f"Költség: {szum} Ft")