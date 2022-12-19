import sys

sys.setrecursionlimit(10**6)
n,m = map(int,sys.stdin.readline().split())

rootL = [i for i in range(n+1)]

def findRoot(node):
    if(rootL[node] != node):
        rootL[node] = findRoot(rootL[node])
    
    return rootL[node]

def union(node1,node2):
    root1 = findRoot(node1)
    root2 = findRoot(node2)
    if(root1 != root2):
        if(root1<root2):
            rootL[root2] = root1
        else:
            rootL[root1] = root2

def isUnion(node1,node2):
    root1 = findRoot(node1)
    root2 = findRoot(node2)
    if(root1 != root2):
        return False
    else:
        return True

for _ in range(m):
    ftn,node1,node2 = map(int,sys.stdin.readline().split())
    if(ftn == 0):
        union(node1,node2)
    else:
        if(isUnion(node1,node2)):
            print("YES")
        else:
            print("NO")

