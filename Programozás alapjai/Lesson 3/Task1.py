# Importáljuk a math csomagot
import math

# Bekérjük az egenlet konstansait
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# kiszámoljuk a diszkriminánst
d = b **2 -4 * a * c

# Ha 0-nál nagyobb akkor kiszámoljuk a két gyököt, amit kiírunk
if d > 0:
    x1 = (b * -1 + math.sqrt(d)) / (2 * a)
    x2 = (b * -1 - math.sqrt(d)) / (2 * a)
    print(f"x1: {x1} x2: {x2}")

# Ha 0 akkor kiszámoljuk az egy gyököt, amit kiírunk
elif d == 0:
    x = (b* -1)/(2*a)
    print(f"X: {x}")

# Ha 0-nél kisebb akkor kiírjuk, hogy nincs megoldás
else:
    print("Nincs megoldás")