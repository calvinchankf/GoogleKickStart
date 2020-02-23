import sys

"""
    python2: binary search
"""
def solve(a, b):
    m = (a + b) / 2
    print(m)
    sys.stdout.flush() # flush
    s = raw_input()
    if s == "CORRECT":
        return
    elif s == "TOO_SMALL":
        a = m + 1
    else:
        b = m - 1
    solve(a, b)

T = input()
for _ in range(T):
    a, b = map(int, raw_input().split())
    _ = input()
    solve(a + 1, b)


# """
#     python3
# """
# def solve(a, b):
#     m = (a + b) // 2
#     print(m)
#     sys.stdout.flush() # flush
#     s = input()
#     if s == "CORRECT":
#         return
#     elif s == "TOO_SMALL":
#         a = m + 1
#     else:
#         b = m - 1
#     solve(a, b)

# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split())
#     _ = int(input())
#     solve(a + 1, b)