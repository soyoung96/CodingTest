import sys

n,k = map(int,sys.stdin.readline().split())

dp = [[0] * (n+1) for _ in range(k+1)]

weights = [-1]
valids = [-1]

for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    weights.append(w)
    valids.append(v)

for y in range(1,n+1):
    for x in range(k+1):
        if(x+weights[y]<=k):
            dp[x+weights[y]][y] = max(dp[x+weights[y]][y-1],dp[x][y-1]+valids[y])
        dp[x][y] = max(dp[x][y],dp[x][y-1])

maxV = -1

for x in range(k+1):
    if(dp[x][-1]>maxV):
        maxV = dp[x][-1]

print(maxV)