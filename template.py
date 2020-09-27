"""
    1st approach:

    Time    
    Space   
"""
def f():
    pass

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    arr = [int(s) for s in raw_input().split(" ")]
    k = int(raw_input())
    res = f(arr, k)
    print("Case #{}: {}".format(t, res))
    # Or
    print(f"Case #{t}: {res}")
    
