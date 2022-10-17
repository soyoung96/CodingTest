import sys
import heapq

n,m,c = map(int,sys.stdin.readline().split())
INF = int(1e9)
inputL = [[] for _ in range(n+1)] #인접 그래프
distL = [INF] * (n+1)


for _ in range(m):
    start,end,t = map(int,sys.stdin.readline().split())
    inputL[start].append((t,end))

h =[]
heapq.heappush(h,(0,c))

while h:
    t,end = heapq.heappop(h)
    if(t>distL[end]):
        continue
    else:
        distL[end] = t #갱신
        for eltT,eltEnd in inputL[end]:
            newT = t + eltT
            if(distL[eltEnd]>newT):#갱신해야함
                distL[eltEnd] = newT
                heapq.heappush(h,(newT,eltEnd))

contryCount=0
maxT = -1
for i in distL:
    if(0<i<INF):
        contryCount+=1
        if(maxT<i):
            maxT=i

print(contryCount,maxT)


