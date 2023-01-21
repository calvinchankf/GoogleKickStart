from math import *

"""
    1st: Sieve of Eratosthenes

    Time    O(sqrt(N))
    Space   O(sqrt(N)) MLE for the mega dataset
"""


def f(Z):
    root = ceil(sqrt(2*Z))
    primes = gen_primes(root)
    res = 0
    for i in range(1, len(primes)):
        temp = primes[i-1] * primes[i]
        if res < temp <= Z:
            res = temp
    return res


def gen_primes(n):
    if n < 2:
        return 0
    primes = n * [True]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i] == False:
            continue
        for j in range(i*i, n, i):
            primes[j] = False
    res = [i for i in range(n) if primes[i]]
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
