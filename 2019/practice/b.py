"""
    python3

    2nd: sliding window
    
    WTF does it mean????
    At the end of each day, one section of the wall will be destroyed. 
    It is always a section of wall that is adjacent to only one other section and is unpainted 

    Question explain:
    At the end of every day, either one of the wall from both ends will be detroyed
    e.g.

    day0: ABCDEF
    day1: xBCDEF or ABCDEx
"""

def f(nums):
    N = len(nums)
    halfLen = (N + 1)//2
    windowSum = sum(nums[:halfLen])
    res = windowSum
    for i in range(halfLen, N):
        windowSum += nums[i] - nums[i-halfLen]
        res = max(res, windowSum)
    return res

T = int(input())
for i in range(1, T + 1):
    _ = int(input())
    scores = [int(s) for s in input()]
    res = f(scores)
    print("Case #{}: {}".format(i, res))