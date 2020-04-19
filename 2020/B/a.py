"""
    1st approach: array

    Small   Pass
    Big     Pass
"""
def f(nums):
    res = 0
    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            res += 1
    return res

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    _ = int(raw_input())
    arr = [int(s) for s in raw_input().split(" ")]
    res = f(arr)
    print("Case #{}: {}".format(i, res))

