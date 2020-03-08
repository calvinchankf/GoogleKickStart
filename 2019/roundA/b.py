import sys
"""
    1st: BFS
    Wrong answer
"""
import sys
"""
    1st: BFS
"""
def solve(grid):
    maxDist = 0
    maxDistI = None
    maxDistJ = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                continue
            steps = bfs(grid, i, j)
            if steps > maxDist:
                maxDist = steps
                maxDistI = i
                maxDistJ = j
    # print(maxDist, maxDistI, maxDistJ)
    if maxDistI == None or maxDistJ == None:
        return 0
    grid[maxDistI][maxDistJ] = 1
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                continue
            steps = bfs(grid, i, j)
            res = max(res, steps)
    return res

def bfs(grid, x, y):
    ht = set()
    q = [(x, y, 0)]
    while len(q) > 0:
        i, j, steps = q.pop(0)
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            continue
        if (i, j) in ht:
            continue
        ht.add((i, j))
        if grid[i][j] == 1:
            return steps
        for di, dj in [(0,-1),(0,1),(1,0),(-1,0)]:
            q.append((i+di, j+dj, steps+1))
    return sys.maxsize

T = int(raw_input())
for i in range(T):
    r, c = map(int, raw_input().split())
    grid = []
    for _ in range(r):
        temp = [int(c) for c in raw_input()]
        grid.append(temp)
    res = solve(grid)
    print("Case #{}: {}".format(i+1, res))

a = [
    [1,0,1],
    [0,0,0],
    [1,0,1],
]
print(solve(a))

a = [
    [1,1]
]
print(solve(a))

a = [
    [1,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,1],
]
print(solve(a))

# a = [
#     [1,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [1,0,0,0,0,1],
# ]
# print(solve(a))

# a = [
#     [1,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [1,0,0,0,0,1],
# ]
# print(solve(a))