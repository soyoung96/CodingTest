import sys
import math
k,n = map(int,sys.stdin.readline().split())

kL = []
for _ in range(k):
    kL.append(int(sys.stdin.readline()))

start = 0
end = int(math.pow(2,31))

def isN(mid,kL): #10000
    answer =0
    for kLE in kL:
        answer+=(kLE//mid)
    return answer

answerMax = -1
while(start<=end):#10000log1000000000
    mid = (start+end)//2
    # print(start,end,mid)
    midN = isN(mid,kL)
    # print(midN)
    if(midN<n):#어쩔 수 없이 줄여야함
        end = mid-1
    else: # 늘려봅세
        start = mid+1
        if(answerMax<mid):
            answerMax = mid
        

print(answerMax)



