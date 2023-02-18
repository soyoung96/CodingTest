import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

visitedL = [False for _ in range(100001)]
premove = [-1 for _ in range(100001)]
def bfs(visitedL,startNode,goal):
    visitedL[startNode] =True #방문

    q = deque([])
    q.append((startNode,0))

    while(q):
        node,dist = q.popleft()
        if(node == goal):
            return dist
        for route in range(3):
            if(route == 0):
                nextNode = node+1
            elif(route == 1):
                nextNode = node -1
            else:
                nextNode = node*2
            if(0<=nextNode<=100000):
                if(not visitedL[nextNode]):
                    visitedL[nextNode] = True
                    q.append((nextNode,dist+1))
                    premove[nextNode] = node

firstAns = bfs(visitedL,n,k)

print(firstAns)

mapAns = []
node = k
mapAns.append(node)
while(premove[node] != -1):
    node = premove[node]
    mapAns.append(node)

for rvsInd in range(len(mapAns)-1,-1,-1):
    print(mapAns[rvsInd],end = " ")



