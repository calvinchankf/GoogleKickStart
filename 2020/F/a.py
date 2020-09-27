"""
    1st approach: math + hashtable

    Time O(N)
    Space O(N)
"""
def f(A, X):
    ht = defaultdict(list)
    for i in range(len(A)):
        d = A[i] // X
        if A[i] % X > 0:
            d += 1
        ht[d].append(i + 1)
    freq = []
    for k in ht:
        freq.append((k, ht[k]))
    freq.sort()
    # print(freq)
    res = []
    for d, arr in freq:
        res += [str(idx) for idx in arr]
    return res

# a = [2, 7, 4]
# b = 3
# print(f(a, b))

# a = [9, 10, 4, 7, 2]
# b = 6
# print(f(a, b))

# a = [9, 10, 4, 7, 2]
# b = 3
# print(f(a, b))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N, X = [int(s) for s in raw_input().split(" ")]
    A = [int(s) for s in raw_input().split(" ")]
    res = f(A, X)
    print("Case #{}: {}".format(t, ' '.join(res)))
    
