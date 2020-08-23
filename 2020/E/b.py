"""
    1st approach: array construction???
    - basically when there is a tie, we see all of the buildings with the same height
    - so we can
        - use 3 to indicate all the buildings which can be seen from both sides C
        - use 2 to indicate the buildings from either A or B perspective
        - use 1 to indicate the unseen buildings
    - we can build the heights for A, B and C first, and then insert the remaining buildings with height 1 some where in the middle

    Time    O(N)
    Space   O(N)
"""
def f(N, A, B, C):

    a = A - C
    b = B - C

    if C > A or C > B or a + b + C > N:
        return 'IMPOSSIBLE'

    if a + b + C == 1 and N >= 2:
        return 'IMPOSSIBLE'

    if N == 1:
        return '1'
    elif N == 2:
        if C == 2:
            return '1 1'
        elif A == 2:
            return '1 2'
        elif B == 2:
            return '2 1'
    else:
        res = []
        for i in range(a):
            res.append(2)
        for i in range(C):
            res.append(3)
        for i in range(b):
            res.append(2)
        remain = N - (A + B - C)
        if remain > 0:
            res = res[:1] + (remain * [1]) + res[1:]
        return ' '.join([str(x) for x in res])

t = int(raw_input())
for i in range(1, t + 1):
    arr = [int(s) for s in raw_input().split(" ")]
    res = f(*arr)
    print("Case #{}: {}".format(i, res))
    

print(f(4,1,3,1))
print(f(4,4,4,3))
print(f(5,3,3,2))
print("-----")
print(f(14,5,7,3))
print(f(1,1,1,1))
print(f(5,1,1,1))
print(f(5,2,2,2))
print(f(5,3,3,3))

print(f(5,4,2,2))
print(f(5,2,4,2))
print(f(5,4,2,1))
print(f(5,2,4,1))