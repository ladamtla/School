# Importáljuk a math csomagot
import math

# Bekérjük a sugár értékét
r = int(input("Add meg a kör sugarát: "))

# Kiszámojuk az értékeket és 2 tízedesjegyre kerekítjük az értékeket
k = round((2 * r * math.pi), 2)
t = round((r ** 2 * math.pi), 2)

# Kiíratjuk a konzolra
print(f"A kör kerülete {k}, a területe {t}")