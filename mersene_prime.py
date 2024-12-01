def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_mersenne_primes(limit):
    mersenne_primes = []
    p = 2
    while (2 ** p - 1) <= limit:
        mersenne_number = 2 ** p - 1
        if is_prime(mersenne_number):
            mersenne_primes.append(mersenne_number)
        p += 1
    return mersenne_primes


limit = 100000
print(find_mersenne_primes(limit))
