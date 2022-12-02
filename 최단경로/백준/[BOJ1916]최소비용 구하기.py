import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e11)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start,end,cost = map(int,sys.stdin.readline().split())
    graph[start].append((cost,end))

h = []

startN,endN = map(int,sys.stdin.readline().split())

heapq.heappush(h,(0,startN))

distL = [INF for _ in range(n+1)]

while(h):
    cost,node = heapq.heappop(h)
    if(distL[node]<=cost):
        continue
    else:
        distL[node] = cost
        for ncost,nnode in graph[node]:
            if(distL[nnode]>cost+ncost):
                heapq.heappush(h,(cost+ncost,nnode))

print(distL[endN])

