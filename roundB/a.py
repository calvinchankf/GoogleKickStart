"""
    1st approach: hashtable

    Time    O(kn)
    Space   O(n)
    5points Passed
    12points Failed
"""


def isP(s, i, j):
    temp = s[i:j]
    return temp == temp[::-1]


def canP(s, i, j):
    i = i - 1
    if isP(s, i, j) == True:
        return True
    ht = {}
    for c in s[i:j]:
        if c not in ht:
            ht[c] = 1
        else:
            ht[c] += 1
    hasOdd = False
    for key in ht:
        if ht[key] % 2 > 0:
            if hasOdd == False:
                hasOdd = True
            else:
                return False
    return True


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    a = [int(s) for s in raw_input().split(" ")]
    s = raw_input()
    count = 0
    for j in range(a[1]):
        c = [int(x) for x in raw_input().split(" ")]
        temp = canP(s, c[0], c[1])
        if temp == True:
            count += 1

    print("Case #{}: {}".format(i, count))
