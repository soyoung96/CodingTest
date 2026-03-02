import sys
from collections import deque

dx = (1,-1,0,0)
dy = (0,0,-1,1)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if(nx<0 or nx>=n or ny<0 or ny>=m or graph[nx][ny]==0):
                continue
            if(graph[nx][ny]==1):
                graph[nx][ny]= graph[x][y] + 1
                queue.append((nx,ny))

    for i in range(n):
        print(graph[i])
    return graph[n-1][m-1]

n,m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(0,0))