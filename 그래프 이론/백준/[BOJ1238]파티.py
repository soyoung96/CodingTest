import sys
import heapq

n,m,x = map(int,sys.stdin.readline().split())
INT = int(1e11)
graph=[[] for _ in range(n+1)]
graph2=[[] for _ in range(n+1)]
dists = [INT for _ in range(n+1)]
dists2 = [INT for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int,sys.stdin.readline().split())
    graph[s].append((t,e))
    graph2[e].append((t,s))

priorQ = []

heapq.heappush(priorQ,(0,x))

while(priorQ): #O(10000log10000)
    t,e = heapq.heappop(priorQ)
    if(dists[e]>t):
        dists[e] = t #갱신
        for nt,ne in graph[e]:
            if(dists[ne]>nt+t):
                heapq.heappush(priorQ,(nt+t,ne))

heapq.heappush(priorQ,(0,x))

while(priorQ):#O(10000log10000)
    t,e = heapq.heappop(priorQ)
    if(dists2[e]>t):
        dists2[e] = t #갱신
        for nt,ne in graph2[e]:
            if(dists2[ne]>nt+t):
                heapq.heappush(priorQ,(nt+t,ne))


maxDist = -1
for ind in range(1,n+1):#O(1000)
    if(maxDist<dists[ind]+dists2[ind]):
        maxDist = dists[ind]+dists2[ind]

print(maxDist)

    










