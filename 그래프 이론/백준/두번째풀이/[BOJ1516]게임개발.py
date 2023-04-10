import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)] #500*500

buildTL = [-1 for _ in range(n+1)] #500

ansBuildTL = [-1 for _ in range(n+1)]

indegreeL = [0 for _ in range(n+1)] #500

for node in range(1,n+1): #500
    inputL = deque(map(int,sys.stdin.readline().split())) #500
    # print(inputL)
    inputL.pop()
    # print(inputL)
    buildTL[node] = inputL.popleft()
    # print(buildTL[node])
    while(inputL):
        preNode = inputL.popleft()
        graph[preNode].append(node)
        indegreeL[node] +=1
        # print("?")


que = deque([])

for node in range(1,n+1):
    if(indegreeL[node] == 0):
        que.append((node,buildTL[node])) #(방문노드, 짓는 데 걸리는 시간)
        ansBuildTL[node] = buildTL[node] #이전 단계에서 최대로 오래 걸린 T로 자신의 건설 시간 계산됌
# print(ansBuildTL)
while(que):
    node,nodeT = que.popleft()
    for nNode in graph[node]:
        indegreeL[nNode]-=1
        if(ansBuildTL[nNode]<nodeT+buildTL[nNode]):
            ansBuildTL[nNode] = nodeT+buildTL[nNode] #이전 단계에서 최대로 오래 걸린 T로 자신의 건설 시간 계산됌
            # print(nNode, ansBuildTL[nNode])
        if(indegreeL[nNode] == 0):
            que.append((nNode,ansBuildTL[nNode])) #(방문노드, 짓는 데 걸리는 시간)

# print(ansBuildTL)
for node in range(1,n+1):
    print(ansBuildTL[node])












    
    
        