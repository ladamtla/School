def time_in_sec(time):
    m, s = time.split(sep=":")
    m = int(m)
    s = int(s)
    return m*60+s

def best_time(times):
    return min(times)

times = []
while True:
    time = input("Adj meg egy időt '12:34' formátumban (kilépés a *-al): ")
    if time == "*":
        break
    else:
        try:
            sec = time_in_sec(time)
        except:
            print("Beviteli hiba!")
            continue
        else:
            times.append(sec)

print("Összes idők (sec-ben)", times)
print("Legjobb idő: ", best_time(times), " sec")

