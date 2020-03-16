"""
    1st: prefix sum + stack
    - b.png

    ref:
    - https://stackoverflow.com/questions/7770945/largest-rectangular-sub-matrix-with-the-same-number
    - https://stackoverflow.com/questions/6945105/search-matrix-for-all-rectangles-of-given-dimensions-select-blocks-of-seats/7353193#7353193

    Time    O(RC)
    Space   O(N)

    6points     Passed
    12points    Failed
"""
def largestRectangleArea(heights):
    res = 0
    # begining with -1, such that we can calculate the range, i - stack[-1][0] - 1, easier
    stack = [(-1, 0)] # (index, height)
    for i in range(len(heights)):
        cur = heights[i]
        if cur > stack[-1][1]:
            # if current height is taller, append to the stack
            stack.append((i, cur))
        else:
            # pop the stack if the items which is > cur height
            while stack[-1][1] > cur:
                popIdx, popH = stack.pop()
                width = i - stack[-1][0] - 1
                area = popH * width
                res = max(res, area)
            # put the current item to the array
            stack.append((i, cur))
    # if the stack is not empty, pop the items
    while len(stack) > 1:
        popIdx, popH = stack.pop()
        width = len(heights) - stack[-1][0] - 1
        area = popH * width
        res = max(res, area)
    return res

def prefixSumOnEachRow(grid):
    r = len(grid)
    c = len(grid[0])
    rows = [c * [1] for _ in range(r)]
    for i in range(r):
        for j in range(1, c):
            if grid[i][j] == grid[i][j-1]:
                rows[i][j] = rows[i][j-1] + 1
    return rows

def extractColumns(matrix):
    r = len(matrix)
    c = len(matrix[0])
    cols = []
    for j in range(c):
        col = []
        for i in range(r):
            col.append(matrix[i][j])
        cols.append(col)
    return cols

def f(grid):
    matrix = prefixSumOnEachRow(grid)
    cols = extractColumns(matrix)
    res = 0
    for col in cols:
        area = largestRectangleArea(col)
        res = max(res, area)
    return res

# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# t = int(input())  # read a line with a single integer
# for idx in range(1, t + 1):
#     r, c, k = [int(s) for s in raw_input().split(" ")]

#     matrix = []
#     for _ in range(r):
#         row =[int(s) for s in raw_input().split(" ")]
#         matrix.append(row)
    
#     print("Case #{}: {}".format(idx, f(matrix)))

a = [
    [3,1,3,3]
]
print(f(a))

a = [
    [4,4,5],
    [7,6,6]
]
print(f(a))

a = [
    [2,2,4,4,20],
    [8,3,3,3,12],
    [6,6,3,3,3],
    [1,6,8,6,4]
]
print(f(a))