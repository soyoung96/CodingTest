import sys
from collections import deque

# sys.setrecursionlimit(int(1e5))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
r,c = map(int,sys.stdin.readline().split())

graph = []

# for _ in range(r):
#     graph.append(list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())))

for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

def chkX(x):
    if(0<=x<r):
        return True
    else:
        return False
    
def chkY(y):
    if(0<=y<c):
        return True
    else:
        return False

maxCnt = -1

# dpL = [0 for _ in range(26)]
# def dfs(x,y,cnt):
#     global maxCnt
#     dpL[graph[x][y]] = 1
#     if(maxCnt<cnt):
#         maxCnt = cnt
#     for i in range(4):
#         newX = x + dx[i]
#         newY = y + dy[i]
#         if(chkX(newX) and chkY(newY)):
#             if(dpL[graph[newX][newY]] == 0):
#                 dfs(newX,newY,cnt+1)
#                 dpL[graph[newX][newY]] = 0


def bfs(x,y):
    global maxCnt
    q = set()
    q.add((x,y,str(graph[x][y])))

    while(q): #20
        x,y,roots = q.pop()
        if(maxCnt<len(roots)):
            maxCnt = len(roots)

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if(chkX(newX) and chkY(newY)):
                if(graph[newX][newY] not in roots):
                    q.add((newX,newY,roots+graph[newX][newY]))
                    

# dfs(0,0,1)
bfs(0,0)
print(maxCnt)




