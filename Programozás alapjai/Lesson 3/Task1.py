import math


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = b **2 -4 * a * c

if d > 0:
    x1 = (b * -1 + math.sqrt(d)) / (2 * a)
    x2 = (b * -1 - math.sqrt(d)) / (2 * a)
    print(f"x1: {x1} x2: {x2}")
elif d == 0:
    x = (b* -1)/(2*a)
    print(f"X: {x}")
else:
    print("Nincs megoldás")