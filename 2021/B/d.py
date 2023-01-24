from math import gcd
from collections import *

"""
    DFS + binary search

    Time    O(NlogN)
    Space   O(N^2)
"""


def upperBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target >= nums[mid][0]:
            left = mid + 1
        else:
            right = mid
    return right


def f(XYLAs, CWs):
    G = defaultdict(dict)
    for X, Y, L, A in XYLAs:
        G[X][Y] = (L, A)
        G[Y][X] = (L, A)
    # print(G)

    dist_to_1 = defaultdict(list)
    stack = [(1, [])]
    seen = set()
    while len(stack) > 0:
        node, costs = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        dist_to_1[node] = costs
        for nb in G[node]:
            stack.append((nb, costs + [G[node][nb]]))

    for k in dist_to_1:
        dist_to_1[k].sort()
    # print(dist_to_1)

    res = []
    for C, W in CWs:
        j = upperBsearch(dist_to_1[C], W)

        if j == 0:
            res.append(0)
            continue

        temp = dist_to_1[C][:j]
        amounts = [a for _l, a in temp]
        x = amounts[0]
        for i in range(1, len(amounts)):
            x = gcd(x, amounts[i])
        res.append(x)
    return(res)


# a = [
#     [2, 1, 2, 4],
#     [2, 3, 7, 8],
#     [3, 4, 6, 2],
#     [5, 3, 9, 9],
#     [2, 6, 1, 5],
#     [7, 1, 5, 7]
# ]
# b = [
#     [5, 10],
#     [5, 8],
#     [4, 1],
#     [6, 1],
#     [7, 6],
# ]
# print(f(a, b))

# a = [
#     [1, 2, 2, 10],
#     [3, 2, 3, 5],
# ]
# b = [
#     [3, 2],
#     [3, 3]
# ]
# print(f(a, b))

T = int(input())
for t in range(1, T + 1):
    N, Q = [int(s) for s in input().split(" ")]
    XYLAs = []
    for _ in range(N-1):
        temp = [int(s) for s in input().split(" ")]
        XYLAs.append(temp)
    CWs = []
    for _ in range(Q):
        temp = [int(s) for s in input().split(" ")]
        CWs.append(temp)
    res = f(XYLAs, CWs)
    res_str = ' '.join([str(c) for c in res])
    print(f"Case #{t}: {res_str}")
