def f1(N):
    res = [N]
    for i in range(1, N//2+1):
        left = 0
        right = N + 1
        while left <= right:
            mid = (left + right) // 2
            total = (2*i+mid-1)*mid
            if total < 2*N:
                left = mid + 1
            elif total > 2*N:
                right = mid - 1
            else:
                res.append(i)
                break
    return len(res)


print(f1(10))
print(f1(125))
print(f1(9009))
print(f1(10000))


# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     res = f1(N)
#     print(f"Case #{t}: {res}")

"""
Testing

> python3 main.py < ts1_input.txt
> python3 main.py < ts2_input.txt
"""
# T = int(input())
# output = open("ts1_output.txt", "r")
# for t in range(1, T + 1):
#     N = int(input())
#     res = f1(N)
#     S = f"Case #{t}: {res}"
#     T = output.readline().strip()
#     if str(S) == str(T):
#         print('Passed')
#     else:
#         print(S, "Failed", T)
# output.close()
