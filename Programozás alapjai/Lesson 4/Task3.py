
# Definiáljuk a két válltozónkat
num = 0
szum = 0

# A ciklus mindaddig fut amíg üres sztringet adunk be neki
# Ha nem üres sztring a bemenet, akkor egyessével hazzáadja a beírt számokat, majd kéri a következőt
while True:
    num = input("Adj meg egy számot: ")
    if num == "":
        break
    else:
        num = int(num)
        szum = szum + num

# Kiírjuk az eredményt
print(f"A beírt számok összege: {szum}")