import math
from collections import *

def f(M):
    res = 0
    for i in range(3):
        row = M[i]
        if row[0] + row[2] == row[1] * 2:
            res += 1
    for j in range(3):
        if M[0][j] + M[2][j] == M[1][j] * 2:
            res += 1
    ctr = Counter()
    dirs = [(0,0,2,2), (0,2,2,0), (1,0,1,2), (0,1,2,1)]
    for a, b, c, d in dirs:
        val = M[a][b] + M[c][d]
        if (val // 2) * 2 == val:
            ctr[val] += 1
    
    if len(ctr.values()) > 0:
        res += max(ctr.values())
    return res

# a = [
#     [3, 4, 11],
#     [10, math.inf, 9],
#     [-1, 6, 7]
# ]
# print(f(a))

# a = [
#     [4, 1, 6],
#     [3, math.inf, 5],
#     [2, 5, 6]
# ]
# print(f(a))

# a = [
#     [9, 9, 9],
#     [9, math.inf, 9],
#     [9, 9, 9]
# ]
# print(f(a))

T = int(input())
for t in range(1, T + 1):
    M = []
    for i in range(3):
        row = [int(c) for c in input().split()]
        if i == 1:
            row.insert(1, math.inf)
        M.append(row)
    res = f(M)
    print(f"Case #{t}: {res}")

"""
Testing

> python3 main.py < ts1_input.txt
> python3 main.py < ts2_input.txt
"""
# T = int(input())
# output = open("ts2_output.txt", "r")
# for t in range(1, T + 1):
#     M = []
#     for i in range(3):
#         row = [int(c) for c in input().split()]
#         if i == 1:
#             row.insert(1, math.inf)
#         M.append(row)
#     res = f(M)
#     S = f"Case #{t}: {res}"
    
#     T = output.readline().strip()
#     if str(S) == str(T):
#         print('Passed')
#     else:
#         print(S, "Failed", T)
#         print(M)
# output.close()