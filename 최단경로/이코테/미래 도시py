import sys
import pprint

n,m = map(int,sys.stdin.readline().split())
INF = int(1e9)
inputL=[[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    start,end = map(int,sys.stdin.readline().split())
    inputL[start][end] = 1
    inputL[end][start] = 1

x,k = map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    inputL[i][i] =0

for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            inputL[start][end] = min(inputL[start][end],inputL[start][mid]+inputL[mid][end])

answer = inputL[1][k]+inputL[k][x]
if(answer >= INF):
    print(-1)
else:
    print(answer)

