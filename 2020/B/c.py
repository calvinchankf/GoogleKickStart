"""
    1st: lc394 but both recursion and stack based solution fail with MLE

    Small   Pass
    Big     MLE
"""

def solve(s):
#     chars = []
#     for c in s:
#         chars.append(c)
#     return dfs(chars)

# def dfs(chars):
#     res = ''
#     num = 0
#     while len(chars) > 0:
#         pop = chars.pop(0)
#         if pop.isdigit():
#             num = num*10 + int(pop)
#         elif pop == '(':
#             res += num * dfs(chars)
#             num = 0
#         elif pop == ')':
#             return res
#         else:
#             res += pop
#     return res
    cntStack = []
    strStack = [""]
    num = 0
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c == '(':
            cntStack.append(num)
            num = 0
            strStack.append("")
        elif c == ')':
            cnt = cntStack.pop()
            cur = strStack.pop()
            temp = cnt * cur
            strStack[-1] += temp
        else:
            strStack[-1] += c
    return strStack.pop()

print(solve('SSSEEE'))
print(solve('N'))
print(solve('N3(S)N2(E)N'))
print(solve('2(3(NW)2(W2(EE)W))'))

def f(s):
    intructions = solve(s)
    toDown = 0
    toRight = 0
    for c in intructions:
        if c == 'N':
            toDown -= 1
        elif c == 'S':
            toDown += 1
        elif c == 'W':
            toRight -= 1
        elif c == 'E':
            toRight += 1
    # h = 1 + toDown
    # w = 1 + toRight
    h = (toDown + 10**9 ) % 10**9
    w = (toRight + 10**9 ) % 10**9
    return w + 1, h + 1

print(f('SSSEEE'))
print(f('N'))
print(f('N3(S)N2(E)N'))
print(f('2(3(NW)2(W2(EE)W))'))

# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# t = int(raw_input())  # read a line with a single integer
# for i in range(1, t + 1):
#     arr = raw_input()
#     res = f(arr)
#     print("Case #{}: {} {}".format(i, res[0], res[1]))


print("-----")

"""
    2nd:
    - stack only
    - dont unfold the characters

    Small   Pass
    Big     Pass
"""

def f(s):
    toDown = 0
    toRight = 0

    curPrefixProduct = 1
    cntStack = []
    num = 0
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c == '(':
            cntStack.append(num)
            curPrefixProduct *= num
            num = 0
        elif c == ')':
            cnt = cntStack.pop()
            curPrefixProduct /= cnt
        else:
            if c == 'N':
                toDown -= curPrefixProduct
            elif c == 'S':
                toDown += curPrefixProduct
            elif c == 'W':
                toRight -= curPrefixProduct
            elif c == 'E':
                toRight += curPrefixProduct
    
    
    h = (toDown + 10**9 ) % 10**9
    w = (toRight + 10**9 ) % 10**9
    return w + 1, h + 1

# print(f('SSSEEE'))
# print(f('N'))
# print(f('N3(S)N2(E)N'))
# print(f('2(3(NW)2(W2(EE)W))'))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    arr = raw_input()
    res = f(arr)
    print("Case #{}: {} {}".format(i, res[0], res[1]))