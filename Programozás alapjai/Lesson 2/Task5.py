import math

# Bekérjük a befogók hosszát
b1 = int(input("Add meg az egyik befogót: "))
b2 = int(input("Add meg a másik befogót: "))

# Kiszámoljuk az átfogót
a = math.sqrt(b1 ** 2 + b2 ** 2)

# Kiíratjuk a konzolra
print(f"Az átfogó hossza: {a}")