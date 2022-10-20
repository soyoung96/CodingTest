import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

INF=int(1e9)
inputMat = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if(inputMat[a][b]>c):  #주어지는 간선 동일한 간선이 있다면 최소 cost 로 맞춘다
        inputMat[a][b] = c

for i in range(n+1):
    inputMat[i][i] =0 

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            inputMat[a][b] = min(inputMat[a][b],inputMat[a][k]+inputMat[k][b])

for x in range(1,n+1):
    for y in range(1,n+1):
        if(inputMat[x][y] == INF):
            inputMat[x][y] = 0
        print(inputMat[x][y],end = " ")
    print()
    
