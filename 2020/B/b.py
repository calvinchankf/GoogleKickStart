"""
    math

    Small   Pass
    Big     Pass
"""

def f(nums, D):
    rightMost = D
    for i in range(len(nums)-1, -1, -1):
        rightMost = nums[i] * (rightMost // nums[i])
    return rightMost

# a = [3, 7, 2]
# print(f(a, 10))

# a = [11, 10, 5, 50]
# print(f(a, 100))

# a = [1,1]
# print(f(a, 1))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    N, D = [int(s) for s in raw_input().split(" ")]
    arr = [int(s) for s in raw_input().split(" ")]
    res = f(arr, D)
    print("Case #{}: {}".format(i, res))