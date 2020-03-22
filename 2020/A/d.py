"""
    the basic idea is use a trie, the below code doesnt work tho

    WA
"""
class Node(object):
    def __init__(self, is_word):
        self.children = 26*[None]
        # self.prefixLen = prefixLen
        self.count = 0
        self.is_word = is_word

class Trie(object):

    def __init__(self):
        self.root = Node(False)

    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            idx = ord(c) - ord('A')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur.count += 1
            cur = cur.children[idx]
        cur.count += 1
        cur.is_word = True

class Solution(object):
    
    def __init__(self):
        self.res = 0
    
    def f(self, arr, k):
        t = Trie()
        for word in arr:
            t.insert(word)

        def dfs(node, path):
            if node == None:
                return
            alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            maxCount = 0
            for i in range(len(node.children)):
                child = node.children[i]
                if child != None:
                    maxCount = max(maxCount, child.count)
                dfs(child, path + alphabets[i])
            # print(path, node.count)
            if node != t.root and node.count >= k and node.count != maxCount:
                self.res += len(path) * (node.count // k)
                # print(node.count, maxCount, len(path), path)
        
        dfs(t.root, '')
        return self.res



# s = Solution()
# a = ['KICK', 'START']
# b = 2
# print(s.f(a, b))

# s = Solution()
# a = ['G', 'G', 'GO', 'GO', 'GOO', 'GOO', 'GOOO', 'GOOO']
# b = 2
# print(s.f(a, b))

# s = Solution()
# a = [
#     'RAINBOW',
#     'FIREBALL',
#     'RANK',
#     'RANDOM',
#     'FIREWALL',
#     'FIREFIGHTER',
# ]
# b = 3
# print(s.f(a, b))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # N, K
    n, k = [int(s) for s in raw_input().split(" ")]
    # arr
    arr = []
    for _ in range(n):
        arr.append(raw_input())
    s = Solution()
    res = s.f(arr, k)
    print("Case #{}: {}".format(i, res))