# (eladasi_osszeg + veteli_osszeg)/(eladasi_osszeg/eladasi_arf + veteli_osszeg/veteli_arf )


.........................................................................................................


def calc_rate(buy_rate, sell_rate, sell_a, buy_a):
    summ = 0
    for br, sr, sa, ba in buy_rate, sell_rate, sell_a, buy_a:
        mid_rate = (sa + ba)/ ((sa/sa) + (ba / br))
        summ = summ + mid_rate
    return summ / len(buy_a)



buying_rate = [374.45, 371.45, 372.5, 373.8]
selling_rate = [389.6, 388.4, 390.5, 394.5]
selling_amount = [1000, 5000, 4000, 4000]
buying_amount = [6000, 7000, 8000, 10000]

print(calc_rate(buying_rate, selling_rate, selling_amount, buying_amount))

