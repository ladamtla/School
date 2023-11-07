def currConverterFromHUF (amount, curr):
    final = 0
    if curr == "CHF": final = amount/406.42
    elif curr == "EUR": final = amount/386.77
    elif curr == "USD": final = amount/366.92
    else: final = -1

    return final

amount = int(input("Adj meg egy összeget forintban: "))
curr = input("Add meg a cél valutát 3 nagybetűvel: ")
final = currConverterFromHUF(amount, curr)
if final >= 0:
    print(f"{amount} HUF egyenlő {round(final, 3)} {curr}")
else:
    print("Valuta nem létezik, vagy hibás megadás!")

