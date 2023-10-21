# Definiáljuk a függvényt
def key ():
    sum = 0

    # Végig iterálunk 0-tól 1000-ig minden számon, ha osztható 3-al vagy 5-el akkor hoszzáadjuk az összeghez
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# Kiírjuk a meghívott függvényt
print(key())