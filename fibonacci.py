import numpy as np
import time

# Recursive Memoization Fibonacci
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Matrix Exponentiation Fibonacci
def matrix_fibonacci(n):
    def matrix_mult(A, B):
        return np.dot(A, B)

    def matrix_power(matrix, power):
        result = np.identity(len(matrix), dtype=int)
        base = matrix

        while power:
            if power % 2 == 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            power //= 2

        return result

    F = np.array([[1, 1], [1, 0]], dtype=int)
    if n == 0:
        return 0
    result = matrix_power(F, n-1)
    return result[0][0]

# Iterative Fibonacci
def iterative_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Testing and Timing
n = 10

# Timing Recursive Memoization
start_time = time.time()
fibo_memo = fibonacci(n)
memo_duration = time.time() - start_time
print(f"Fibonacci number at position {n} using memoization is {fibo_memo} (Time: {memo_duration:.6f} seconds)")

# Timing Matrix Exponentiation
start_time = time.time()
fibo_matrix = matrix_fibonacci(n)
matrix_duration = time.time() - start_time
print(f"Fibonacci number at position {n} using matrix exponentiation is {fibo_matrix} (Time: {matrix_duration:.6f} seconds)")

# Timing Iterative Method
start_time = time.time()
fibo_iter = iterative_fibonacci(n)
iter_duration = time.time() - start_time
print(f"Fibonacci number at position {n} using iteration is {fibo_iter} (Time: {iter_duration:.6f} seconds)")


# Output
# Fibonacci number at position 10 using memoization is 55 (Time: 0.000006 seconds)
# Fibonacci number at position 10 using matrix exponentiation is 55 (Time: 0.000037 seconds)
# Fibonacci number at position 10 using iteration is 55 (Time: 0.000002 seconds)
