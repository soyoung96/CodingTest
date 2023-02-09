import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e11)

graph=[[] for _ in range(n+1)]

for _ in range(m): #O(1e5)
    s,e,cost = map(int,sys.stdin.readline().split())
    graph[s].append((cost,e))

startN,endN = map(int,sys.stdin.readline().split())

dp=[[INF,[]] for _ in range(n+1)]

priorQ=[]
heapq.heappush(priorQ,(0,[startN]))

while(priorQ):#O(1e5*log(1e3))
    cost,nodes =heapq.heappop(priorQ)
    if(dp[nodes[-1]][0]>cost):
        dp[nodes[-1]][0] = cost
        dp[nodes[-1]][1] = nodes
        for nextCost,nextNode in graph[nodes[-1]]:
            newCost = nextCost+cost
            newNodes = nodes+[nextNode]
            if(dp[nextNode][0]>newCost):
                heapq.heappush(priorQ,(newCost,newNodes))

print(dp[endN][0])
print(len(dp[endN][1]))
for node in dp[endN][1]:
    print(node,end=" ")






