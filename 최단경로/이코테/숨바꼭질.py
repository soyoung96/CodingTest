import sys
import heapq

n,m = map(int,sys.stdin.readline().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1,node2 = map(int,sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

distance = [INF for _ in range(n+1)]

priorQ = []

heapq.heappush(priorQ,(0,1))

while priorQ:
    dist,node = heapq.heappop(priorQ)
    if(distance[node]<=dist):
        continue
    else:
        distance[node] = dist
        for nextNode in graph[node]:
            heapq.heappush(priorQ,(dist+1,nextNode))


maxDist = -1
maxInd = 0

for ind,dist in enumerate(distance):
    if(dist != INF):
        if(maxDist<dist):
            maxInd = ind
            maxDist = dist

sameCount =0
for dist in distance:
    if(maxDist==dist):
        sameCount+=1


print(maxInd,end = " ")
print(maxDist,end = " ")
print(sameCount,end = " ")

