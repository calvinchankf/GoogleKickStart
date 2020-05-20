"""
    Approach: topological ordering

    Time    O(N+E) N: number of nodes, E: number of edges

    Small       Pass
    Big         Pass
"""
def f(m):

    edges = []
    nodeSet = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i > 0 and m[i-1][j] != m[i][j]:
                edges.append((m[i][j], m[i-1][j]))
            nodeSet.add(m[i][j])

    nodes = list(nodeSet)
    connections = {}
    indegrees = {}
    for node in nodes:
        connections[node] = []
        indegrees[node] = 0
    # get all the adjacents list and indegree
    for src, dest in edges:
        connections[src].append(dest)
        indegrees[dest] += 1
    # get the nodes with 0 indegree
    queue = []
    for key in indegrees:
        if indegrees[key] == 0:
            queue.append(key)
    # dequeue node from the queue and put it into the result
    res = []
    while len(queue) > 0:
        node = queue.pop(0)
        res.append(node)
        children = connections[node]
        for child in children:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                queue.append(child)
    # return -1 if there is a cycle
    for key in indegrees:
        if indegrees[key] > 0:
            return -1
    return ''.join(res)


a = [
    'ZOAAMM',
    'ZOAOMM',
    'ZOOOOM',
    'ZZZZOM'
]
print(f(a))

a = [
    'XXOO',
    'XFFO',
    'XFXO',
    'XXXO',
]
print(f(a))

a = [
    'XXX',
    'XPX',
    'XXX',
    'XJX',
    'XXX'
]
print(f(a))

a = [
    'AAABBCCDDE',
    'AABBCCDDEE',
    'AABBCCDDEE',
]
print(f(a))

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    R, C = [int(s) for s in raw_input().split(" ")]
    m = []
    for _ in range(R):
        m.append(raw_input())
    res = f(m)
    print("Case #{}: {}".format(i, res))