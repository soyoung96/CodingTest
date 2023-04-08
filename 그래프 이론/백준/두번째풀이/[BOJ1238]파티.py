import sys
import heapq

def dickstra(startNode,distL,priorQ,graph):
    heapq.heappush(priorQ,(0,startNode))
    while(priorQ):
        dist,node = heapq.heappop(priorQ)
        if(dist<distL[node]):
            distL[node] = dist
            for nNode,nDist in graph[node]:
                if(nDist+dist<distL[nNode]):
                    heapq.heappush(priorQ,(nDist+dist,nNode))


INF = int(1e9)
n,m,x= map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

distL = [INF for _ in range(n+1)]
distL2 = [INF for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int,sys.stdin.readline().split())
    graph[s].append((e,t))
    graph2[e].append((s,t))

priorQ = []

dickstra(x,distL,priorQ,graph)
dickstra(x,distL2,priorQ,graph2)

answer = -1

for ind in range(1,n+1):
    if(answer<distL[ind]+distL2[ind]):
        answer = distL[ind]+distL2[ind]

print(answer)












