import sys
from pprint import pprint

n,m = map(int,sys.stdin.readline().split())
INF = int(1e11)
dp = [[INF] * (n+1) for _ in range(n+1)]

for ind in range(1,n+1): #100
    dp[ind][ind] = 0

for _ in range(m): #5000
    a,b = map(int,sys.stdin.readline().split())
    dp[a][b] = 1
    dp[b][a] = 1

for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            dp[start][end] = min(dp[start][end],dp[start][mid]+dp[mid][end])

answer = -1
minOfSumE = INF 
for ind,elts in enumerate(dp): #100
    sumE=sum(elts[1:])
    if(minOfSumE>sumE):
        minOfSumE = sumE
        answer = ind
print(answer)
