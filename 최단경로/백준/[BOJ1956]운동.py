import sys
from pprint import pprint

v,e = map(int,sys.stdin.readline().split())

INF = int(1e11)

graph = [ [INF]*(v+1) for _ in range(v+1)]

# for ind in range(1,v+1):
#     graph[ind][ind] = 0 #싸이클 찾을 땐 이거 필요 없음

for _ in range(e): #O(400*400)
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = c

for mid in range(1,v+1): #O(400*400*400)
    for start in range(1,v+1):
        for end in range(1,v+1):
            graph[start][end] = min(graph[start][end],graph[start][mid]+graph[mid][end])

ans = int(1e13)
# pprint(graph)
for city in range(1,v+1): #O(400*400)
    ans = min(ans,graph[city][city])

if(ans >= int(1e11)): #실수 조심 
    print(-1)
else:
    print(ans)





