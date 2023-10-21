# Definiáljuk a függvényt
def key ():
    sum = 0

    # Végig iterálunk 0-tól 1000-ig minden számon
    for i in range(0,1001):

        # Ha osztható 3-al az össezghez hozzáadjuk a vizsgált (i) számot
        if i % 3 == 0:
            sum = sum + i
        # Ha osztható 5-al az össezghez hozzáadjuk a vizsgált (i) számot
        if i % 5 == 0:
            sum = sum + i
        # Ha mindkettővel osztható akkor kivonjuk belőle a vizsgált számot (mivel akkor 2x lett hozzáadva)
        if i % 5 == 0 and i % 3 == 0:
            sum = sum - i
    return sum

# Kiírjuk a meghívott függvényt
print(key())