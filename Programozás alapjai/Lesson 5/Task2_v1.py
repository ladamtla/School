def key ():
    sum = 0
    for i in range(0,1001):
        if i % 3 == 0:
            sum = sum + i
        if i % 5 == 0:
            sum = sum + i
        if i % 5 == 0 and i % 3 == 0:
            sum = sum - i
    return sum

print(key())