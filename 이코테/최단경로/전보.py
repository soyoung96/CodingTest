import heapq

n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist,node = heapq.heappop(q)
    if(dist > distance[node]):
      continue
    else:
      for i in graph[node]:
        toNode,gDist =i
        newDist = gDist + dist
        if(newDist<distance[toNode]):
          distance[toNode] = newDist
          heapq.heappush(q,(newDist,toNode))

dijkstra(c)

count =0

maxT=-1
for i in distance:
  if(i != INF):
    count+=1
    if(maxT<i):
      maxT = i

print(count-1,maxT)


  
  