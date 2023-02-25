import sys

n,m,k = map(int,sys.stdin.readline().split())

moneys = list(map(int,sys.stdin.readline().split()))

realMoneys = []
for ind,money in enumerate(moneys):
    realMoneys.append((money,ind+1))

realMoneys.sort()

roots = [i for i in range(n+1)]

def findRoot(node,roots):
    if(roots[node] != node):
        roots[node] = findRoot(roots[node],roots)
    return roots[node]

def union(node1,node2,roots):
    root1 = findRoot(node1,roots)
    root2 = findRoot(node2,roots)
    if(root1 != root2):
        if(root1 < root2):
            roots[root2] = root1
        else:
            roots[root1] = root2
        return True #합칠 수 있음
    else:
        return False #합칠 수 없음

for _ in range(m):
    v,w = map(int,sys.stdin.readline().split())
    union(v,w,roots)

sumMoneyE =0
for moneyE,friend in realMoneys:
    if(union(0,friend,roots)):
        sumMoneyE+=moneyE

if(sumMoneyE>k):
    print("Oh no")
else:
    print(sumMoneyE)






