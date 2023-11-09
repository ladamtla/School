def is_monotone_inc(prices: list) -> bool:
    found = False
    for i in range(len(prices)-1):
        if prices[i] > prices[i+1]:
            found = True
    return not found


prices = [384, 386, 388, 389, 389, 390]
print(is_monotone_inc(prices))
