"Csak a hiba számításhoz"
import math

def fact(num):
    fact = 1
    while num > 0:
        fact = (fact * num)
        num -= 1
    return fact

def sin_cos_calculator(m, x):
    """
    :param m: MacLaurin sor fokszáma
    :param x: szám 
    :return: szám sinusza, koszinusza
    """
    sders = [0, 1, 0, -1]
    cders = [1, 0, -1, 0]
    ssin = 0
    scos = 0

    while m >= 0:
        scos += (cders[m % 4] / fact(m)) * x ** m
        ssin += (sders[m % 4] / fact(m)) * x ** m

        m -= 1

    return ssin, scos


m = int(input("Adja meg a MacLaurin sor fokszámát: "))
x = int(input("Adjon meg egy számot: "))
sin, cos = sin_cos_calculator(m, x)
print(f"A {x} szinusza: {round(sin, 10)} - hiba: {abs(math.sin(x)-sin)}")
print(f"A {x} koszinusza: {round(cos, 10)} - hiba: {abs(math.cos(x)-cos)}")
