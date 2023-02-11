import sys

sys.setrecursionlimit(int(1e5))
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

mList = []

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    mList.append((c,a,b))

mList.sort() #1e5*log(1e5)

roots = [i for i in range(n+1)]

def findRoot(node,roots):
    if(roots[node]!=node):
        roots[node] = findRoot(roots[node],roots)
    return roots[node]

def union(node1,node2):
    root1 = findRoot(node1,roots)
    root2 = findRoot(node2,roots)
    if(root1!=root2):
        if(root1>root2):
            roots[root1] = root2
        else:
            roots[root2] = root1
        return True
    else:
        return False

ans =0
for c,a,b in mList:
    if(union(a,b)):
        ans+=c

print(ans)
