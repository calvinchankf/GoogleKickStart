def f(arr):
    diffs = []
    for i in range(1, len(arr)):
        d = arr[i] - arr[i-1]
        diffs.append(d)
    j = 0
    res = 0


# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     arr = [int(c) for c in input().split(' ')]
#     res = f(arr)
#     print(f"Case #{t}: {res}")
