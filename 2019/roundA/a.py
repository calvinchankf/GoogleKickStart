import sys
"""
    1st: sort + prefix sum

    Test set 1: Pass
    Test set 2: Pass
"""
def solve(arr, k):
    arr.sort()
    windowSum = 0
    for i in range(k):
        windowSum += arr[k-1] - arr[i]
    res = windowSum
    for i in range(k, len(arr)):
        leftMostDiff = arr[i-1] - arr[i-k]
        windowSum -= leftMostDiff
        windowSum += (k-1) * (arr[i] - arr[i-1])
        res = min(res, windowSum)
    return res

T = int(raw_input())
for i in range(T):
    n, p = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    res = solve(arr, p)
    print("Case #{}: {}".format(i+1, res))

# print(solve([3,1,9,100], 3))
# print(solve([5,5,1,2,3,4], 2))
# print(solve([7,7,1,7,7], 5))