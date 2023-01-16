"""
    2 tricks
    - we just need to rotate the matrix 3 times to count 4 directions: 
        the L shape: # of 1 above + # of 1 on the right
    - to speed up, use prefix sum from above + prefix sum from the right

    Time    O(7RC)
    Space   O(RC)
"""


def f(matrix):
    res = 0

    M = matrix
    for _ in range(4):
        R, C = len(M), len(M[0])
        ones_from_above, ones_from_right = prefixSum2D(M)
        for i in range(R):
            for j in range(C):
                count_above = ones_from_above[i][j]
                count_right = ones_from_right[i][j]
                res += max(0, min(count_above//2, count_right) - 1)
                res += max(0, min(count_right//2, count_above) - 1)
        M = rotate90(M)
    return res


def rotate90(matrix):
    R, C = len(matrix), len(matrix[0])
    res = [R * [0] for _ in range(C)]
    for i in range(C):
        for j in range(R):
            res[i][j] = matrix[R-j-1][i]
    return res


def prefixSum2D(matrix):
    R, C = len(matrix), len(matrix[0])
    ones_from_above = [C * [0] for _ in range(R)]
    ones_from_right = [C * [0] for _ in range(R)]
    for j in range(C):
        pfs = 0
        for i in range(R):
            if matrix[i][j] == 0:
                pfs = 0
            pfs += matrix[i][j]
            ones_from_above[i][j] = pfs
    for i in range(R):
        pfs = 0
        for j in range(C-1, -1, -1):
            if matrix[i][j] == 0:
                pfs = 0
            pfs += matrix[i][j]
            ones_from_right[i][j] = pfs
    return (ones_from_above, ones_from_right)


T = int(input())
for t in range(1, T + 1):
    R, C = [int(s) for s in input().split(" ")]
    matrix = []
    for _ in range(R):
        rows = [int(s) for s in input().split(" ")]
        matrix.append(rows)
    res = f(matrix)
    print(f"Case #{t}: {res}")

"""
Testing

> python3 main.py < ts1_input.txt
> python3 main.py < ts2_input.txt
"""
# T = int(input())
# output = open("ts1_output.txt", "r")
# for t in range(1, T + 1):
#     R, C = [int(s) for s in input().split(" ")]
#     matrix = []
#     for _ in range(R):
#         rows = [int(s) for s in input().split(" ")]
#         matrix.append(rows)
#     res = f(matrix)
#     S = f"Case #{t}: {res}"
#     T = output.readline().strip()
#     if str(S) == str(T):
#         print('Passed')
#     else:
#         print(S, "Failed", T)

# output.close()
