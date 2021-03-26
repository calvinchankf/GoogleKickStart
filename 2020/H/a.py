"""
    1st approach: Math

    Time    O(N)
    Space   O(1)
"""
def f(N, K, S):
    # completed + restart + all
    a = (K - 1) + 1 + N
    # completed + go back + all remaining
    b = (K - 1) + (K - S) + (N - S + 1)
    return min(a, b)

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N, K, S = [int(s) for s in raw_input().split(" ")]
    res = f(N, K, S)
    print("Case #{}: {}".format(t, res))
    