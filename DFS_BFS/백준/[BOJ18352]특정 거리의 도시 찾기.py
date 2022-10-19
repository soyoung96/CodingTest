import sys
from collections import deque

n,m,k,x = map(int,sys.stdin.readline().split())

inputM = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    inputM[a].append(b)


def bfsFindCostK(inputM,x,k):
    q = deque([])
    cost =0
    q.append((x,cost))
    visited[x] = True #해당 노드 방문
    answer = []
    while(q):
        start,cost = q.popleft()
        if(cost == k):
            answer.append(start)
        for nextNode in inputM[start]:
            if(not visited[nextNode]):
                q.append((nextNode,cost+1)) #거리 증가하고 해당 노드 방문
                visited[nextNode] = True #해당 노드 방문
    
    
    return answer


answer = bfsFindCostK(inputM,x,k)
if(len(answer)==0):
    print(-1)
else:
    answer.sort()
    for elt in answer:
        print(elt)


