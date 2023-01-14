import heapq

"""
    max heap + bfs
    - start from the tallest cells, itereate its neighbous and by assigning the height with H-1 and put them in the maxheap
    - in each BFS, we only iterate if the height is correct
"""


def f(matrix):
    R, C = len(matrix), len(matrix[0])
    pq = []
    for i in range(R):
        for j in range(C):
            heapq.heappush(pq, (-matrix[i][j], i, j))

    cache = []
    for i in range(R):
        cache.append(matrix[i][:])

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(pq) > 0:
        h, i, j = heapq.heappop(pq)

        # only iterate if the height is correct (top down from its previous cell)
        # look at below that we assign cache[_i][_j] = cache[i][j] - 1
        if cache[i][j] != -h:
            continue

        for di, dj in dirs:
            _i, _j = i+di, j+dj
            if _i < 0 or _i >= R or _j < 0 or _j >= C:
                continue
            # update the height of neighbours
            if cache[_i][_j] < cache[i][j] - 1:
                cache[_i][_j] = cache[i][j] - 1
                heapq.heappush(pq, (-cache[_i][_j], _i, _j))

    # print(cache)
    res = 0
    for i in range(R):
        for j in range(C):
            res += cache[i][j] - matrix[i][j]
    return res


# a = [[3, 4, 3]]
# print(f(a))

# a = [[3, 0, 0]]
# print(f(a))

# a = [
#     [0, 0, 0],
#     [0, 2, 0],
#     [0, 0, 0],
# ]
# print(f(a))

# a = [
#     [0, 0, 0],
#     [0, 2, 2],
#     [0, 0, 0],
# ]
# print(f(a))

# a = [
#     [0, 0, 0],
#     [0, 3, 0],
#     [0, 0, 0],
# ]
# print(f(a))

# a = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 4, 0],
#     [0, 0, 0, 0]
# ]
# print(f(a))

# a = [
#     [2, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 2],
#     [0, 0, 0, 0],
# ]
# print(f(a))

# a = [
#     [100, 0, 0, 0, 0, 0, 0, 0, 101]
# ]
# print(f(a))

# a = [
#     [100],
#     [0],
#     [0],
#     [0],
#     [0],
#     [0],
#     [0],
#     [0],
#     [0],
#     [101],
# ]
# print(f(a))

# a = [
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
# ]
# print(f(a))

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
