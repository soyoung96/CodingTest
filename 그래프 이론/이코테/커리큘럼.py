# from heapq import heappop
import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

result =0

for i in range(1,n+1):
    inputL = list(map(int,sys.stdin.readline().split()))
    cost =0
    indegreeElt = 0
    for ind,elt in enumerate(inputL):
        if(elt ==-1): #다음줄 입력으로 넘어감
            break
        else:
            if(ind==0): #cost
                cost = elt
            else: #선수과목 
                graph[elt].append(i) #인접그래프 연결
                indegreeElt +=1 #진입차수 증가
    
    indegree[i] = [cost,indegreeElt]

q=deque([]) 

for start in range(1,n+1):
    if(indegree[start][1] == 0): #start의 진입차수 0이면
        q.append((indegree[start][0],start)) #(start의 비용,start) 큐 집어넣음

costL = [0] * (n+1)

while q:
    cost,start = q.popleft()
    costL[start] = cost
    for end in graph[start]:
        costL[end] = max(costL[end],cost + indegree[end][0])
        indegree[end][1]-=1 #진입차수 줄이기
        if(indegree[end][1] == 0): # 새로운 진입차수 0 된거 우선 순위 큐에 집어넣기
            q.append((costL[end],end)) # 이떄 cost는 선수 과목중 시간이 가장 많이 걸리는 cost!


for i in range(1,n+1):
    print(costL[i])
    


    
            
    




