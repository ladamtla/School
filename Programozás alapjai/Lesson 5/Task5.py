# Idő beolvas függvény, ha minden tartománynak megfelel akkor formázott sztinget ad vissza
def ido_beolvaso():
    while True:
        h = int(input("Óra: "))
        m = int(input("Perc: "))
        s = int(input("Másodperc: "))
        if h in range(0, 24) and m in range(0, 60) and s in range(0, 60):
            break
        else:
            print("Nem megfelelő értékek, próbáld újra")
            continue
    return f"{h}:{m}:{s}"

# Kiszámolja az összes másodpercet
def time_in_sec(time):
    h, m, s = time.split(sep=":")
    h = int(h)
    m = int(m)
    s = int(s)
    return h*3600+m*60+s

# Kiszámolja az összes percet
def time_in_min(time):
    h, m, s = time.split(sep=":")
    h = int(h)
    m = int(m)
    s = int(s)
    return h*60+m+s/60

# Kiszámolja az összes órát
def time_in_hour(time):
    h, m, s = time.split(sep=":")
    h = int(h)
    m = int(m)
    s = int(s)
    return h+m/60+s/3600

# Egymás után meghívjuk a 4 függvényt
time = ido_beolvaso()
sec = time_in_sec(time)
min = time_in_min(time)
hour = time_in_hour(time)

# Formázottan kiírjuk a 4 függvény értékeit
print(f"{time} összesen {sec} másodpec, vagy {min} perc, vagy {hour} óra.")
