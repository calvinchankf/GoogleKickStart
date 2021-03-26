"""
    1st approach: brute force
"""
def f(L, R):
    res = 0
    cur = L
    while cur <= R:
        if isBoring(cur):
            res += 1
        cur += 1
    return res

def isBoring(n):
    s = str(n)
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] in '02468':
                return False
        else:
            if s[i] in '13579':
                return False
    return True
# print(f(5, 15))
# print(f(120, 125))
# print(f(779, 783))

"""
    2nd: recursion to generate the numbers

    still LTE for large data set
"""
class Solution(object):

    def countBoringNumbers(self, L, R):
        self.res = 0
        for i in range(1, 10, 2):
            self.dfs(L, R, str(i), 1)
        return self.res

    def dfs(self, L, R, cur, idx):
        if L <= int(cur) <= R:
            # print('dfs', cur)
            self.res += 1
        if int(cur) > R:
            return
        if (idx + 1) % 2 == 1:
            self.dfs(L, R, cur + '1', idx + 1)
            self.dfs(L, R, cur + '3', idx + 1)
            self.dfs(L, R, cur + '5', idx + 1)
            self.dfs(L, R, cur + '7', idx + 1)
            self.dfs(L, R, cur + '9', idx + 1)
        else:
            self.dfs(L, R, cur + '0', idx + 1)
            self.dfs(L, R, cur + '2', idx + 1)
            self.dfs(L, R, cur + '4', idx + 1)
            self.dfs(L, R, cur + '6', idx + 1)
            self.dfs(L, R, cur + '8', idx + 1)

print(Solution().countBoringNumbers(5, 15))
print(Solution().countBoringNumbers(120, 125))
print(Solution().countBoringNumbers(779, 783))
print(Solution().countBoringNumbers(99, 100000000))


# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# T = int(raw_input())  # read a line with a single integer
# for t in range(1, T + 1):
#     L, R = [int(s) for s in raw_input().split(" ")]
#     res = f(L, R)
#     print("Case #{}: {}".format(t, res))
    