"""
    1st approach: string

    Time    O(N)   
    Space   O(1)
"""
def f(S):
    count = 0
    kickCount = 0
    for i in range(len(S)):
        if S[i:i+4] == 'KICK':
            kickCount += 1
        elif S[i:i+5] == 'START':
            count += kickCount
    return count

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    S = raw_input()
    res = f(S)
    print("Case #{}: {}".format(t, res))
    
