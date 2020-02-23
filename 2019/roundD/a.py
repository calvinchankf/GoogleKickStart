"""
    1st approach: brute force

    Time    O(n^3)
    Space   O(n)

    TLE
"""


def f(arr, modies):
    res = []
    for i in range(len(modies)):
        idx, num = modies[i]
        arr[idx] = num
        # find largest xor-sum of a subarray that is an even
        maxCount = 0
        for j in range(len(arr)):
            xor = 0
            for k in range(j, len(arr)):
                xor ^= arr[k]
                c = hammingWeight(xor)
                if c % 2 == 0:
                    count = k-j+1
                    maxCount = max(maxCount, count)
        res.append(str(maxCount))
    return res


def hammingWeight(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count


a = [10, 21, 3, 7]
b = [[1, 13], [0, 32], [2, 22]]
# print(f(a, b))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # N, Q
    nq = [int(s) for s in raw_input().split(" ")]
    # arr
    arr = [int(s) for s in raw_input().split(" ")]
    modies = []
    for j in range(nq[1]):
        modi = [int(x) for x in raw_input().split(" ")]
        modies.append(modi)
    # print("hi", arr, modies)
    c = f(arr, modies)
    res = " ".join(c)

    print("Case #{}: {}".format(i, res))
