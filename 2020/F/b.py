"""
    1st approach: sort intervals

    Time    
    Space   
"""
def f(intvs, K):
    intvs.sort()
    res = 0
    maxEnd = 0
    for i in range(len(intvs)):
        s, e = intvs[i]
        if e < maxEnd:
            continue
        diff = e - max(s, maxEnd)
        c = diff//K
        if diff%K > 0:
            c += 1
        if c > 0:
            res += c
            maxEnd = max(s, maxEnd) + c*K
    return res

# a = [(3,5), (1,5), (10,11)]
# b = 5
# print(f(a, b))

# a = [(1,2), (3,5), (13,14)]
# b = 2
# print(f(a, b))

# a = [(1,3), (4,10)]
# b = 2
# print(f(a, b))

# a = [(1,10)]
# b = 2
# print(f(a, b))

# a = [(1,10), (2,20)]
# b = 2
# print(f(a, b))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N, K = [int(s) for s in raw_input().split(" ")]
    intvs = []
    for _ in range(N):
        s, e = [int(s) for s in raw_input().split(" ")]
        intvs.append((s, e))
    res = f(intvs, K)
    print("Case #{}: {}".format(t, res))
    
