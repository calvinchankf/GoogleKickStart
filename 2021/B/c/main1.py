from math import *

"""
    2nd: math
    - the search range is between:
            lower bound: sqrt(N) - 2 * prime gap
            upper lound: srqrt(N) + prime gap
        so, we can just search the adjacent pairs in between
    - for mega-dataset, we cannot use Sieve of Eratosthenes because it takes linear space O(N),
        so, we can use Primlity Test OR Segemented Sieve to check if a number is a prime (6k + i)
    - https://en.wikipedia.org/wiki/Primality_test

    Time    O(sqrt(N) / 6)
    Space   O(1)
"""


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


def find_next_prime(n):
    if n < 2:
        return 2
    prime = n if n % 2 else n - 1
    while True:
        prime += 2
        if is_prime(prime):
            return prime


def f(Z):
    a = find_next_prime(int(Z**0.5) - 2*288)
    b = find_next_prime(a)
    res = 0
    while a*b <= Z:
        res = max(res, a*b)
        a, b = b, find_next_prime(b)
    return res


# print(f(2021))
# print(f(2020))
# print(f(10**9))
# print(f(10**18))

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    res = f(N)
    print(f"Case #{t}: {res}")
