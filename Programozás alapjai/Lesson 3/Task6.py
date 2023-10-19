# Bekérünk egy pontszámot
point = int(input("Írj be egy pontszámot: "))

# Ha a pontszám a megfelelő tartományban van, egyessével megvizsgáljuk, hogy melyik intervallumokba esik bele
if point < 0 or point > 100:
    print("Hibás pontszám")
else:
    if point < 60:
        jegy = 1
    elif point >= 60 and point < 70:
       jegy = 2
    elif point >= 70 and point < 80:
       jegy = 3
    elif point >= 80 and point < 90:
       jegy = 4
    elif point >= 90:
       jegy = 5

    # Majd kiírjuk az érdemjegyet
    print(f"Érdemjegy: {jegy}")