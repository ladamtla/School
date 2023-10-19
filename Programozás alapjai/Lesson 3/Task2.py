# Bekérjük a 3 oldalt
a = input("a oldal: ")
b = input("b oldal: ")
c = input("c oldal: ")

# Megvizsgáljuk, hogy bármely 2 oldal összege nagyobb-e, mint a 3. oldal, ha igen, akkor háromszög.
if a+b>c and a+c>b and b+c>a:
    print("Ez egy valós háromszög")
else:
    print("Nem létezik ilyen háromszög")