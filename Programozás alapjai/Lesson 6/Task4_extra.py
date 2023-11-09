def average_calculator (jegyek):
    return sum(jegyek)/len(jegyek)
def kredit_a_calculator (jegyek):
    szum = 0
    kredit = 5*len(jegyek)
    for jegy in jegyek:
        szum = szum + jegy*5
    return szum/kredit

jegyek = []
i = 0
while i < 6:
    try:
        jegy = input("Adj meg egy jegyet (átlag számítása *-al): ")
        if jegy == "*":
            break
        jegy = int(jegy)
    except:
        print("Egy egész számot adj meg!")
        continue
    else:
        if jegy > 0 and jegy <=5:
            jegyek.append(jegy)
            i += 1
        else:
            print("Hibás jegy! 1-től 5-ig add meg!")
            continue

print("A jegyek átlaga: ", average_calculator(jegyek))
print(f"Összess kredit: {5*len(jegyek)}")
print("A jegyek súlyozott átlaga: ", kredit_a_calculator(jegyek))
