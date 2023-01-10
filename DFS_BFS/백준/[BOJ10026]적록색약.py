import sys
from pprint import pprint

sys.setrecursionlimit(int(1e8)) #재귀 문제 풀때 빠트리지 말것
n = int(sys.stdin.readline())

graph = [["X"] * (n+1)]
visitedGraph = [[0] * (n+1) for _ in range(n+1)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def chkXY(xy):
    if(1<=xy<=n):
        return True
    else:
        return False

def dfs(x,y,graph,visitedGraph,isSick): #isSick true -> 색맹/ O(10000)
    color = graph[x][y]
    visitedGraph[x][y] = 1 #방문
    
    for go in range(4):
        newX = x+dx[go]
        newY = y+dy[go]
        if(chkXY(newX) and chkXY(newY)): #그래프를 벗어나지 않고
            if(visitedGraph[newX][newY] == 0): #방문 아직 안했고
                if(isSick): #색맹이라면
                    if(color == "R" or color == "G"): #색깔이 레드 그린일때
                        if(graph[newX][newY] == "R" or graph[newX][newY] == "G"): #주변 컬러 레드그린이면 방문
                            dfs(newX,newY,graph,visitedGraph,True)
                    else: #색깔 파랑이라면
                        if(graph[newX][newY] == color): #같은 컬러라면 방문
                            dfs(newX,newY,graph,visitedGraph,True)
                else: #색맹 아니라면
                    if(graph[newX][newY] == color): #같은 컬러라면 방문
                        dfs(newX,newY,graph,visitedGraph,False)

                    

for _ in range(n):
    graph.append(["X"]+list(sys.stdin.readline().rstrip()))

notSickNum = 0
sickNum = 0

for x in range(1,n+1):
    for y in range(1,n+1):
        if(visitedGraph[x][y] == 0): #방문 아직 안했다면
            notSickNum+=1
            dfs(x,y,graph,visitedGraph,False)

visitedGraph = [[0] * (n+1) for _ in range(n+1)]


for x in range(1,n+1):
    for y in range(1,n+1):
        if(visitedGraph[x][y] == 0): #방문 아직 안했다면
            sickNum+=1
            dfs(x,y,graph,visitedGraph,True)

print(notSickNum,sickNum)





        



