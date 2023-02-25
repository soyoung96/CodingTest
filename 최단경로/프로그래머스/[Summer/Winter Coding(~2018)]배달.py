import heapq

INF = int(1e11)

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for roadE in road:
        a,b,c = roadE
        graph[a].append((c,b))
        graph[b].append((c,a))
    
    dist = [INF for _ in range(N+1)]
    priorQ = []
    heapq.heappush(priorQ,(0,1))
    
    while(priorQ):
        cost,node = heapq.heappop(priorQ)
        if(dist[node]>cost):
            dist[node] = cost
            for nCost,nNode in graph[node]:
                newCost = nCost + cost
                if(dist[nNode]>newCost):
                    heapq.heappush(priorQ,(newCost,nNode))
    ans =0
    for ind in range(1,N+1):
        if(dist[ind]<=K):
            ans+=1
    

    return ans