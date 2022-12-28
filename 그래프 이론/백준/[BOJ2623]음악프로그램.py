import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

inDegrees = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

for _ in range(m): #100*1000
    inputL = list(map(int,sys.stdin.readline().split()))
    inputL = inputL[1:]
    for ind in range(len(inputL)-1):
        fromE = inputL[ind]
        toE = inputL[ind+1]
        graph[fromE].append(toE)
        inDegrees[toE] +=1

que = deque([])

for ind,inDegree in enumerate(inDegrees): #1000
    if(inDegree == 0 and ind!=0):
        que.append(ind)


answer = []
while(que): #1000
    node = que.popleft()
    answer.append(node)
    for nextNode in graph[node]:
        inDegrees[nextNode]-=1 #인 차수 감수
        if(inDegrees[nextNode] == 0):#인 차수 0이면
            que.append(nextNode)

if(len(answer)!=n):
    print(0)
else:
    for elt in answer:
        print(elt)

       
