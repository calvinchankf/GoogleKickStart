def f(S):
    res = [1]
    cnt = 1
    for i in range(1, len(S)):
        if S[i] > S[i-1]:
            cnt += 1
        else:
            cnt = 1
        res.append(cnt)
    return ' '.join([str(x) for x in res])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    S = input()
    res = f(S)
    print(f"Case #{t}: {res}")
