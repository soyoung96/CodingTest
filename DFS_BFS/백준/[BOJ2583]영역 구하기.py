import sys
# from pprint import pprint
from collections import deque
# sys.setrecursionlimit(1000000)
m,n,k = map(int,sys.stdin.readline().split())

graph = [[0]*n for _ in range(m)] #10000



dx = [1,-1,0,0]
dy = [0,0,1,-1]
space =0
def chkX(x):
    if(0<=x<n):
        return True
    else:
        return False

def chkY(y):
    if(0<=y<m):
        return True
    else:
        return False

# def dfs(startX,startY,graph):
#     global space
#     graph[startY][startX] = 1 #방문
#     space+=1
#     # pprint(graph)
#     for go in range(4):
#         newX,newY = startX+dx[go],startY+dy[go]
#         if(chkX(newX) and chkY(newY)):
#             if(graph[newY][newX]!=1):
#                 dfs(newX,newY,graph)

def bfs(startX,startY,graph):
    global space
    q = deque([(startX,startY)])
    graph[startY][startX] = 1 #방문
    space+=1 
    while(q):
        startX,startY = q.popleft()
        for go in range(4):
            newX,newY = startX+dx[go],startY+dy[go]
            if(chkX(newX) and chkY(newY)):
                if(graph[newY][newX]!=1):
                    graph[newY][newX] = 1 #방문
                    space+=1 
                    q.append((newX,newY))



for _ in range(k):#1000000
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[y][x] = 1
# pprint(graph)

ansL = []
num =0
for startX in range(n):
    for startY in range(m):
        if(graph[startY][startX]!=1):
            space=0
            num+=1
            # dfs(startX,startY,graph)
            bfs(startX,startY,graph)
            ansL.append(space)

print(num)
for elt in sorted(ansL):
    print(elt,end=" ")



