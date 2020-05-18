"""
    1st: brute force

    For test set 1, we can use the brute force approach to generate all subarray sums,
    check if each one is a square and return the total count. 
    This would be enough to pass all the test cases under the time complexity.
    ^ it is not, i got LTE
"""
def isPerfectSquare(num):
    left = 1
    right = num
    while left <= right:
        mid = (left + right)//2
        if mid*mid < num:
            left = mid + 1
        elif mid*mid > num:
            right = mid - 1
        else:
            return True
    return False

def f(arr):
    res = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == 0 or isPerfectSquare(s):
                res += 1
    return res

a = [2, 2, 6]
print(f(a))

a = [30, 30, 9, 1, 30]
print(f(a))

a = [4, 0, 0, 16]
print(f(a))

a = [4, -10, 12, 16, 20, -42, 32]
print(f(a))

# t = int(raw_input())  # read a line with a single integer
# for i in range(1, t + 1):
#     _ = raw_input()
#     arr = [int(s) for s in raw_input().split(" ")]
#     res = f(arr)
#     print("Case #{}: {}".format(i, res))

print("-----")

from collections import defaultdict

"""
    2nd: hashtbale
    - sum array sum equals to K
    - iterate from j*j = 0 to N * largestNum to get all the squares

    Time    O(N * N^0.5)
    Space   O(N)

    Small       Pass
    Big         LTE

    According to the note from google, the below approach will pass if it is C++ or something else:
    Note: We do not recommend using interpreted/slower languages for the test set 2 of this problem.
"""
def f(nums):
    res = 0
    pfs = 0
    largestNum = 0
    ht = defaultdict(int)
    for i in range(len(nums)):
        pfs += nums[i]
        largestNum = max(largestNum, abs(nums[i]))
        j = 0
        while j*j <= (i + 1) * largestNum:
            k = j * j
            if pfs == k:
                res += 1
            remain = pfs - k
            if remain in ht:
                res += ht[remain]
            j += 1
        ht[pfs] += 1
    return res

a = [2, 2, 6]
print(f(a))

a = [30, 30, 9, 1, 30]
print(f(a))

a = [4, 0, 0, 16]
print(f(a))

a = [4, -10, 12, 16, 20, -42, 32]
print(f(a))

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    _ = raw_input()
    arr = [int(s) for s in raw_input().split(" ")]
    res = f(arr)
    print("Case #{}: {}".format(i, res))

print("-----")