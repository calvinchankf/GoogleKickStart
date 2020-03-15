"""
    1st: hashtable
    - simply put the visited cells in a hashtable
    - following the instruction to traverse the matrix

    Time    O(N^2)
    Space   O(N)

    6points     Passed
    12points    Failed
"""
def f(start_i, start_j, instructions):
    hs = set()
    dirs = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0,-1),
    }
    i, j = start_i, start_j
    hs.add((i, j))
    idx = 0
    while idx < len(instructions):
        head = instructions[idx]
        di, dj = dirs[head]
        i += di
        j += dj
        while (i, j) in hs:
            i += di
            j += dj
        hs.add((i, j))
        idx += 1
    return i, j


# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# t = int(input())  # read a line with a single integer
# for idx in range(1, t + 1):
#     n, r, c, i, j = [int(s) for s in raw_input().split(" ")]
#     s = raw_input()
#     res_i, res_j = f(i, j, s)
#     print("Case #{}: {} {}".format(idx, res_i, res_j))
"""
3
5 3 6 2 3
EEWNS
4 3 3 1 1
SESE
11 5 8 3 4
NEESSWWNESE
"""

# suggested solution: store intervals in hashtable instead of storing i,j
# e.g. https://codereview.stackexchange.com/questions/221119/solution-to-kickstarts-wiggle-walk