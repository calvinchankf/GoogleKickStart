"""
    Greedy + math
    - actually we only need the first half of the string
    - then we can count the number of lexicographical smaller strings by converting the string to a K-based number
    - one corner case is if e.g. S = ABCCBA, then ABCCBA wont be considered

    e.g.1
    S = ABCXYX
    we consider ABCCBA

    e.g.2
    S = ZYXCBA
    we consider ZYXXYZ, and then the sequences like ZYA..., ZYB..., ZYC should be considered

    Time    O(N)
    Space   O(N)
"""


def f(S, K):
    MOD = 10**9 + 7
    N = len(S)
    M = (len(S) + 1)//2
    digits = N * ['']
    for i in range(M):
        digits[i] = S[i]
        digits[N-i-1] = S[i]
    res = 0
    for i in range(M):
        idx = ord(digits[i]) - ord('a')
        res = res*K + idx
        res %= MOD
    T = ''.join(digits)
    res = res + (T < S)
    res %= MOD
    return res


# s = 'bc'
# k = 3
# print(f(s, k))

# s = 'abcdd'
# k = 5
# print(f(s, k))

# s = 'd'
# k = 5
# print(f(s, k))

# s = 'aabbbaab'
# k = 2
# print(f(s, k))

# T = int(input())
# for t in range(1, T + 1):
#     N, K = map(int, input().split(' '))
#     S = input()
#     res = f(S, K)
#     print(f"Case #{t}: {res}")


"""
Testing

> python3 main.py < ts1_input.txt
> python3 main.py < ts2_input.txt
"""
T = int(input())
output = open("ts2_output.txt", "r")
for t in range(1, T + 1):
    N, K = map(int, input().split(' '))
    S = input()
    res = f(S, K)
    X = f"Case #{t}: {res}"
    Y = output.readline().strip()
    if str(X) == str(Y):
        print('Passed')
    else:
        print(X, "Failed", Y, S, K)

output.close()
