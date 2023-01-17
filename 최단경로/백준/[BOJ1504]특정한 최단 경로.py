import sys
import heapq

n,e = map(int,sys.stdin.readline().split())
INF = int(1e11)
graph = [[] for _ in range(n+1)] #O(800)

dp = [INF for _ in range(n+1)] #O(800)

for _ in range(e): #O(200000)
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1,v2 = map(int,sys.stdin.readline().split())

priorQ = []

def dickstra(dp,priorQ,graph,startN,endN):
    
    heapq.heappush(priorQ,(0,startN))

    while(priorQ): #O(400000log400000)
        dist,nNode = heapq.heappop(priorQ)
        if(dp[nNode]>dist):
            dp[nNode] = dist
            for c,b in graph[nNode]:
                newDist = dist+c
                if(dp[b]>newDist):            
                    heapq.heappush(priorQ,(newDist,b)) #방문

    return dp[endN]

firstCase = dickstra(dp[:],priorQ,graph,1,v1) + dickstra(dp[:],priorQ,graph,v1,v2) + dickstra(dp[:],priorQ,graph,v2,n)
secondCase = dickstra(dp[:],priorQ,graph,1,v2) + dickstra(dp[:],priorQ,graph,v2,v1) + dickstra(dp[:],priorQ,graph,v1,n)

if(firstCase >= INF and secondCase >= INF):
    print(-1)
else:
    print(min(firstCase,secondCase))
