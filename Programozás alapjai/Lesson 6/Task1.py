def divisor_count(number):
    count = 0
    for i in range(1, mumber + 1):
        if number % i == 0:
            count += 1
    return count

def is_prime(number):
    return divisor_count(number) == 2

def count_primes(start, end):
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    return count



start = int(input("Start: "))
end = int((input("End: ")))

if start < end:
    print(f"The number of primes: {count_primes(start, end)}")
else:
    print("Start must be greather then end!")