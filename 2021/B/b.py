"""
    3 cases:

    e.g.1 first element
    9  4  6  8  10  12
     -5 +2 +2 +2  +2
    
    e.g.2 last element
    2  4  6  8  10  1
     +2 +2 +2 +2  -9

    e.g.3 element in the middle
    2  4  6  1  10  12
     +2 +2 -5 +9  +2

            -5+9 = +4 which continue the sequence
"""

# a = [2, 2, 2, 2, -9]
# print(solve_end(a))
# a = [6, -3, -3, -3, -3, -3, 2, 2, 2, 2, -9]
# print(solve_end(a))
# a = a[::-1]
# print(solve_end(a))


def solve(diffs):
    n = len(diffs)
    max_cnt = 0
    i = 0
    j = 0
    while i < n:

        # grow until the next diff is not the same
        while j < n and diffs[i] == diffs[j]:
            j += 1
        max_cnt = max(max_cnt, j - i + 1)

        # case 1 and 2
        if j < n:
            max_cnt = max(max_cnt, j - i + 2)

        # case 3
        if j + 1 < n and diffs[j] + diffs[j+1] == 2 * diffs[i]:
            k = j + 2
            while k < n and diffs[k] == diffs[i]:
                k += 1
            max_cnt = max(max_cnt, k - i + 1)

        i = j

    return max_cnt


def f(arr):
    diffs = []
    for i in range(1, len(arr)):
        diffs.append(arr[i] - arr[i-1])

    res = 0
    res = max(res, solve(diffs))
    res = max(res, solve(diffs[::-1]))
    return res


# a = [9, 7, 5, 3]
# print(f(a))

# a = [5, 5, 4, 5, 5, 5, 4, 5, 63]
# print(f(a))

# a = [8, 5, 2, 0]
# print(f(a))

# a = [0, 1, 10, 99, 999, 9999]
# print(f(a))

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [int(c) for c in input().split(' ')]
    res = f(arr)
    print(f"Case #{t}: {res}")
