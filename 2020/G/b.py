"""
    1st approach: 

    Time    O(NN)
    Space   O(2N)
"""
def f(mat):
    N = len(mat)
    res = 0
    heads = set()
    for i in range(N):
        heads.add((0, i))
        heads.add((i, 0))
    for i, j in heads:
        diagSum = 0
        _i, _j = i, j
        while _i < N and _j < N:
            diagSum += mat[_i][_j]
            _i += 1
            _j += 1
        res = max(res, diagSum)
    return res

# a = [
#     [1, 2, 5],
#     [3, 6, 1],
#     [12, 2, 7],
# ]
# print(f(a))

# a = [
#     [0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 0],
#     [2, 2, 2, 8, 0],
#     [1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0],
# ]
# print(f(a))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N = int(raw_input())
    mat = []
    for i in range(N):
        arr = [int(s) for s in raw_input().split(" ")]
        mat.append(arr)
    res = f(mat)
    print("Case #{}: {}".format(t, res))
    