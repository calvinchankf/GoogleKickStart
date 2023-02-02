"""
    1st: binary search

    Time    O(GlogG)
    Space   O(G)
"""


def f1(G):
    res = [G]
    for K in range(1, G//2+1):
        left = 0
        right = G + 1
        while left <= right:
            mid = (left + right) // 2
            total = (2*K+mid-1)*mid
            if total < 2*G:
                left = mid + 1
            elif total > 2*G:
                right = mid - 1
            else:
                res.append(K)
                break
    # print(res)
    return len(res)


# print(f1(10))
# print(f1(125))
# print(f1(9009))
# print(f1(10000))

"""
    2nd: math

    consider:
    (K + K + day - 1) * day = 2G
    (2K + day - 1) * day = 2G
    ^^^^^^^^^^^^^^
    2K + day - 1 = partner
    2K = partner + 1 - day
    K = (partner + 1 - day)//2

    W e just need to find out how many K(s) are divisible by 2

    Time    O(sqrt(G))
    Space   O(1)
"""


def f2(G):
    res = 0  # or res = []
    d = 1
    while d*d <= 2*G:
        if 2*G % d == 0:
            partner = 2*G // d
            K = partner + 1 - d
            if K % 2 == 0 and K > 0:
                res += 1  # or res.append(K//2)
        d += 1
    # so res = [K0, K1,...] e.g. [8, 23, 62, 125]
    return res


# print(f2(10))
# print(f2(125))
# print(f2(9009))
# print(f2(10000))

T = int(input())
for t in range(1, T + 1):
    G = int(input())
    res = f1(G)
    print(f"Case #{t}: {res}")

"""
Testing

> python3 main.py < ts1_input.txt
> python3 main.py < ts2_input.txt
"""
# T = int(input())
# output = open("ts2_output.txt", "r")
# for t in range(1, T + 1):
#     G = int(input())
#     res = f2(G)
#     S = f"Case #{t}: {res}"
#     T = output.readline().strip()
#     if str(S) == str(T):
#         print('Passed')
#     else:
#         print(S, "Failed", T)
# output.close()
