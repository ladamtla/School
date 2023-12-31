
def jegy_szamito(point):
    """
    Kiszámolja egy pont-ból az érdemjegyet
    :param point: pontszám
    :return: érdemjegy
    """
    if point < 0 or point > 100:
        print("Hibás pontszám")
        jegy = 0
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
    return jegy
def multi_jegy_szamito(pontok):
    """
    Kiszámol több pontból, több jegyet. Bemenete és kimenete is lista
    :param pontok: Pontok listában
    :return: Jegyek listában
    """
    jegyek = []
    for point in pontok:
        jegy = jegy_szamito(point)
        jegyek.append(jegy)
    return jegyek
def jegy_szamlalo(jegyek):
    """
    Kiszámolja, a jegyek számát típúsonként
    :param jegyek: Érdemjegyek listában
    :return: Jegy típúsok darabszáma 5 elemű listában 1-5-ig
    """
    one = jegyek.count(1)
    two = jegyek.count(2)
    three = jegyek.count(3)
    four = jegyek.count(4)
    five = jegyek.count(5)
    return [one, two, three, four, five]
def tablazat_rajzolo(jegyek_szama):
    """
    A jegyek darabszámából egy táblázatot rajzol
    :param jegyek_szama: Jegyek darabszáma listában 1-5-ig
    :return: -
    """
    print("---------------")
    print("|-Jegy-|--db--|")
    jegy = 1
    for db in jegyek_szama:
        print(f"|  {jegy}   |   {db}  |")
        jegy += 1
    print("---------------")
def atlag(jegyek):
    """
    Kiszámolja a jegyek átlagát egy listából.
    :param jegyek: lista a jegyekből
    :return: átlag
    """
    szum = 0
    count = 0
    for jegy in jegyek:
        szum = szum + jegy
        count += 1
    return szum / count
def elteres_kiiro(atlag, jegyek):
    """
    Kiszámolja és kiírja a dolgozatok átlagtól való eltérését
    :param atlag: átlag
    :param jegyek: dolgogatok jegyei listában
    :return: -
    """
    count = 1
    for jegy in jegyek:
        print(f"Dolgozat_{count}: {jegy}, eltérés az átlagtól: {jegy-atlag}")
        count += 1
def randompont_generator(db):
    """
    0-100 ig számok között generál egy "db" hosszúságú listát.
    :param db: lista hossza
    :return: random számokkal feltöltött lista
    """
    import random
    pontok = []
    i = 0

    while i < db:
        pont = random.randrange(0, 100)
        pontok.append(pont)
        i += 1
    return pontok



db = int(input("Dolgozatok száma a random generáláláshoz: "))

pontok = randompont_generator(db)

jegyek = multi_jegy_szamito(pontok)
jegyek_szama = jegy_szamlalo(jegyek)

print("Pontok:", pontok)
print("Jegyek egyessével:", jegyek)
print("Jegyek db száma (1-5):", jegyek_szama)
tablazat_rajzolo(jegyek_szama)
print(f"A jegyek átlaga: {atlag(jegyek)}")
elteres_kiiro(atlag(jegyek), jegyek)
