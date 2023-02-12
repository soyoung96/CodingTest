import sys
from collections import deque
import heapq

n,m = map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

inDegrees = [0 for _ in range(n+1)]

for _ in range(m): #O(100000)
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    inDegrees[b]+=1

q = []

for ind,inDegree in enumerate(inDegrees):
    if(inDegree == 0 and ind>=1):
        heapq.heappush(q,ind)

ans =[]
while(q):#O(32000log100000)
    problem = heapq.heappop(q)
    ans.append(problem)
    for nextProblem in graph[problem]:
        inDegrees[nextProblem]-=1
        if(inDegrees[nextProblem] == 0):
            heapq.heappush(q,nextProblem)

for elt in ans:#O(32000)
    print(elt,end=" ")






