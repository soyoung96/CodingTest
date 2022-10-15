import sys

n,m = map(int,sys.stdin.readline().split())

inputL=[]
for _ in range(n):
    inputL.append(int(sys.stdin.readline()))

dp=[-1]*(10000+1)

for i in inputL:
    dp[i] = 1

for i in range(1,m+1):
    minL=[]

    for k in inputL:
        if((i-k)>=0):
            if(dp[i-k] != -1):
                minL.append(dp[i-k]+1)

    if(len(minL)==0): #방법이 없다
        continue
    else:
        dp[i] = min(minL)



print(dp[m])
    
    
