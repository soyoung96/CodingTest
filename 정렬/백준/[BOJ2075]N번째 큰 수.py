import sys
import heapq

n = int(sys.stdin.readline())

priorQ = []
for _ in range(n): #O(1500*1500log1500)
    inputL = list(map(int,sys.stdin.readline().split()))
    for inputE in inputL:
        heapq.heappush(priorQ,inputE) 
        if(len(priorQ) == n+1): #리스트 길이 n+1이상이면
            heapq.heappop(priorQ)  #가장 작은값 하나 빼줌

answer = heapq.heappop(priorQ) #log(1500)

print(answer)
