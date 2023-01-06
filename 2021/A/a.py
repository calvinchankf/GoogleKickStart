"""
    2 pointers

    Time    O(N)
    Space   O(1)
"""


def f(S, K):
    i, j = 0, len(S) - 1
    diff = 0
    while i < j:
        if S[i] != S[j]:
            diff += 1
        i += 1
        j -= 1
    return abs(diff - K)


# print(f("ABCAA", 1))
# print(f("ABAA", 2))
# print(f("AAAAABBBBB", 3))


T = int(input())
for t in range(1, T + 1):
    N, K = [int(s) for s in input().split(" ")]
    S = input()
    res = f(S, K)
    print(f"Case #{t}: {res}")
