def currConverterFromHUF (amount, curr):
    final = 0
    if curr == "CHF": final = amount/406.42
    elif curr == "EUR": final = amount/386.77
    elif curr == "USD": final = amount/366.92
    else: final = -1

    return final

def currConverter(amount, fromcurr, tocurr):
    amounthuf = 0
    if fromcurr == "HUF": amounthuf = amount
    elif fromcurr == "CHF": amounthuf = amount*406.42
    elif fromcurr == "EUR": amounthuf = amount*386.77
    elif fromcurr == "USD": amounthuf = amount*366.92
    else: amounthuf = -1
    if amounthuf >= 0:
        out = currConverterFromHUF(amounthuf, tocurr)
    else:
        out = -1

    return out

amount = int(input("Adj meg egy összeget: "))
fromcurr = input("Add meg, hogy ez milyen valutában van (3 nagy betűvel): ")
tocurr = input("Add meg a cél valutát (3 nagy betűbel): ")

final = currConverter(amount, fromcurr, tocurr)

if final >=0:
    print(f"{amount} {fromcurr} egyenlő {round(final, 2)} {tocurr}")
else:
    print("Valuta nem létezik, vagy hibás megadás!")
