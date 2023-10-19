def is_prime(number):

    if number == 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

while True:
    x = int(input("Adj meg egy számot: "))
    if x > 0:
        break
    else:
        print("Error")
print(is_prime(x))


