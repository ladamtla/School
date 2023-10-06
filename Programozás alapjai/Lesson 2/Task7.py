# Bekérjük az időt, és az időtartamot
time = int(input("Add meg a jelenlegi időt (órában): "))
clock = int(input("Add meg hány óra múlva legyen ébresztés (órában): "))

# Kiszámoljuk az ébresztés idejét, ha nagyobb, mint 24, akkor kivonjuk belőle
alarm = time + clock
if alarm >=24:
    alarm -= 24

# Kiíratjuk a konzolra
print(f"Az ébresztőóra {alarm} órakor fog megszólalni")