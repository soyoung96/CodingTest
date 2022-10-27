import sys
INF = int(1e10)
n,m = map(int,sys.stdin.readline().split())

inputL = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    start,end = map(int,sys.stdin.readline().split())
    inputL[start][end] = 1

for i in range(1,n+1):
    inputL[i][i] = 0

for k in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            inputL[start][end] = min(inputL[start][end],inputL[start][k]+inputL[k][end])

answer =0

for x in range(1,n+1):
    isAnswer = True
    for y in range(1,n+1):
        if(inputL[x][y] == INF and inputL[y][x] ==INF): # x는 순위를 알 수 없는 노드
            isAnswer = False
    
    if(isAnswer):# 노드의 순위 알 수 있으면 
        answer+=1 #정답에 추가

print(answer)
