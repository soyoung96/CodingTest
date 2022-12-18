import sys
import heapq
from pprint import pprint

dx = [0,0,1,-1]
dy = [1,-1,0,0]
INF = int(1e11)

m,n = map(int,sys.stdin.readline().split())
dp = [[INF] * m for _ in range(n)]
graph = []

for _ in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))


priorQ = []
heapq.heappush(priorQ,(0,0,0))

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

while(priorQ):
    cost,x,y = heapq.heappop(priorQ)
    if(cost<dp[x][y]):
        dp[x][y] = cost
        for go in range(4):
            nextX = x+dx[go]
            nextY = y+dy[go]
            if(chkX(nextX) and chkY(nextY)):
                nextCost = cost+graph[nextX][nextY]
                if(nextCost<=dp[nextX][nextY]):
                    heapq.heappush(priorQ,(nextCost,nextX,nextY))

print(dp[n-1][m-1])

