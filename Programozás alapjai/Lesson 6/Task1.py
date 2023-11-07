def is_prime(number):
    """
    Ellenőrzi, hogy egy adott szám prímszám-e
    :param number: Egy szám
    :return: True/False
    """
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

    # Ellenőrzött bemeneten bekérünk egy számot

def count_primes(start, end):
    count = 0
    for num in range(start, end):
        if is_prime(num) == True:
            count += 1
    return count

def is_square(number):
    if number < 0:
        return False
    sqrt = int(number ** 0.5)
    return sqrt * sqrt == number

def count_square(start, end):
    count = 0
    for num in range(start, end):
        if is_square(num) == True:
            count += 1
    return count

def count_negative_or_odd(start, end):
    count = 0
    szum = 0
    for num in range(start, end):
        if num < 0 or num%2 !=0:
            count +=1
            szum += num
    average = szum / count
    return average

def count_positive_or_even(start, end):
    count = 0
    szum = 0
    for num in range(start, end):
        if num > 0 or num%2 == 0:
            count +=1
            szum = szum * num
    average = szum ** (1/count)
    return average

start = int(input("Start: "))
end = int((input("End: ")))

if start < end:
    print(f"Prímek darabszáma: {count_primes(start, end)}")
    print(f"Négyzetszámok darabszáma: {count_square(start, end)}")
    print(f"Negatív vagy páratlan számok számtani átlaga: {count_negative_or_odd(start, end)}")
    print(f"Pozitív vagy páros számok mértani átlaga: {count_negative_or_odd(start, end)}")
else:
    print("A kezdő érték nem lehet nagyobb, mint a befejező érték!")