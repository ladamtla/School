def sumday(date):
    y, m, d = date.split(sep=".")
    szum = 0
    y = int(y)
    m = int(m)
    d = int(d)
    i = 0
    szum = 0

    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(0, m):
        szum = szum + days[i]

    szum = szum + d - days[m - 1]

    return szum


date = input("Dátum: ")
print(f"{date} az év {sumday(date)}. napja.")

