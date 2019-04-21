"""
    1st approach: hashtable

    Time    O(n^2)
    Space   O(n)
    14points Passed
    28points Failed
"""


def maxValue(nums, occurLimit):
    maxCnt = 0
    for i in range(len(nums)):
        curCnt = 0
        ht = {}
        hd = set()  # excluded
        disqCount = 0
        for j in range(i, len(nums)):
            num = nums[j]
            if num not in ht:
                ht[num] = 1
            else:
                if num in hd:
                    disqCount += 1
                    continue
                ht[num] += 1
                if ht[num] > occurLimit:
                    hd.add(num)
                    disqCount += ht[num]

            curCnt = j-i+1 - disqCount
            if curCnt > maxCnt:
                maxCnt = curCnt

    return maxCnt


# a = [1, 1, 4, 1, 4, 4]
# b = 2
# print(maxValue(a, b))

# a = [1, 2, 500, 3, 4, 500, 6, 7]
# b = 1
# print(maxValue(a, b))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    a = [int(s) for s in raw_input().split(" ")]
    b = [int(x) for x in raw_input().split(" ")]
    c = maxValue(b, a[1])
    print("Case #{}: {}".format(i, c))
