# Importáljuk a math csomagot
import math

# Bekérjük a futamidőt
t = int(input("Kérjük, adja meg a futamidőt (években): "))

# Eltároljuk a konstans értékeket
C = 10000  # 10000 Ft
r = 0.08  # 8%
m = 12

# Kiszámítjük a függvény segítségével az eredményt
FV = C * math.pow((1+(r/m)), (m*t))

# Kiíratjuk a konzolra
print(f"A bankbetét értéke a futamidő végén: {FV} Ft")