import sys
import copy
from collections import deque

n = int(sys.stdin.readline())

inputL = list(map(int,sys.stdin.readline().split()))
inputL.sort()
answer = []
min = int(1e11)

for ind in range(n):
    target = inputL[ind]
    start = ind
    end = len(inputL)-1
    breakP = False
    while(start<=end):
        mid = (start+end)//2
        result = target + inputL[mid]
        if(result<0):#오른쪽으로 이동
            start = mid+1
        if(result>0):#왼쪽으로 이동
            end = mid-1
        if(min>abs(result)):
            min = abs(result)
            answer = [target,inputL[mid]]
        if(result == 0):
            breakP = True
            break
    if(breakP):
        break

answer.sort()
print(answer[0],answer[1])



