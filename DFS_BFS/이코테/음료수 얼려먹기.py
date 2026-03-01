import sys

dx = (1,-1,0,0)
dy = (0,0,-1,1)

def dfs(x,y,graph):
    if(x<0 or x>=n or y<0 or y>=m):
        return
    if(graph[x][y] == 0):
        graph[x][y] = 1
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            dfs(nx,ny,graph)
        return True

n,m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
count = 0
for i in range(n):
    for j in range(m):
        if(dfs(i,j,graph)== True):
            count+=1

print(count)