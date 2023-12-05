def oszthatosag_sorozat(szamok):
    # Bemenetként kapott számok sorozatának hossza
    n = len(szamok)

    # 12 elemű kimeneti sorozat inicializálása nullákkal
    kimenet = [0] * 12

    # Számok sorozatának bejárása
    for i in range(n):
        # Az aktuális szám oszthatóságának ellenőrzése az indexszel
        if szamok[i] % (i + 1) == 0:
            # Ha osztható, növeljük az eredmény sorozat megfelelő indexű elemét
            kimenet[i % 12] += 1

    return kimenet


# Példa a függvény használatára
bemenet_sorozat = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
kimenet_sorozat = oszthatosag_sorozat(bemenet_sorozat)
print("Bemenet sorozat:", bemenet_sorozat)
print("Kimenet sorozat:", kimenet_sorozat)