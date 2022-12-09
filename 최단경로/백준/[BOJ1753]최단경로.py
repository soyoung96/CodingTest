import sys
import heapq

v,e = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline())

INF = int(1e11)

graph = [[] for _ in range(v+1)]

for _ in range(e):
    start,end,cost = map(int,sys.stdin.readline().split())
    graph[start].append((cost,end))

pq = []#우선순위 큐

for elt in graph[k]:
    heapq.heappush(pq,elt)

distance = [INF for _ in range(v+1)]

distance[k] = 0

while(pq):
    cost,nextNode = heapq.heappop(pq)
    if(distance[nextNode]>cost):
        distance[nextNode] = cost #거리갱신
        for nextCost,nnextNode in graph[nextNode]:
            if(distance[nnextNode]>nextCost+cost):
                heapq.heappush(pq,(nextCost+cost,nnextNode))

for node in range(1,v+1):
    if(distance[node] != INF):
        print(distance[node])
    else:
        print("INF")


