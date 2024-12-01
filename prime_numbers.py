import random

def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True


number = 67280421310721
print(is_prime_fermat(number))
number2 = 170141183460469231731687303715884105721
print(is_prime_fermat(number2))
number3 = 2**2281 - 1
print(is_prime_fermat(number3))
carmichael = 232250619601
print(is_prime_fermat(carmichael))
carmichael2 = 1012962765146491
print(is_prime_fermat(carmichael2))
carmichael3 = 70368744177643
print(is_prime_fermat(carmichael3))
carmichael4 = 2152302898747
print(is_prime_fermat(carmichael4))

