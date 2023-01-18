import sys

'''
유니온 파인드 기법 쓴 이유
- 양방향 그래프
- 즉 한 집합안에 속하는 노드들이라면 어떤 순서로든 여행가능
'''
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[]]

for _ in range(n): #O(200)
    inputL = [0]+list(map(int,sys.stdin.readline().split()))
    graph.append(inputL)

rootL = [ i for i in range(n+1)] #O(200)

def findRoot(rootL,node):
    if(rootL[node] != node):
        rootL[node] = findRoot(rootL,rootL[node])
    return rootL[node]

def union(node1,node2):
    root1 = findRoot(rootL,node1)
    root2 = findRoot(rootL,node2)
    if(root1 != root2):
        if(root1<root2):
            rootL[root2] = root1
        else:
            rootL[root1] = root2

for x in range(1,n+1):
    for y in range(1,n+1):
        if(graph[x][y] ==1):
            union(x,y)

inputCity = list(map(int,sys.stdin.readline().split()))

representation = rootL[inputCity[0]]

ans = True
for city in inputCity:
    if(representation != rootL[city]):
        ans = False

if(ans):
    print("YES")
else:
    print("NO")







