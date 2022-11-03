import sys
import heapq

dx = [1,-1,0,0]
dy = [0,0,1,-1]
INF =int(1e9)
t = int(sys.stdin.readline())

def chkXY(x):
    if(0<=x<n):
        return True
    else:
        return False

for _ in range(t):
    n = int(sys.stdin.readline())
    minDist = [[INF] * n for _ in range(n)] #최소 비용 행렬
    graph = []

    for _ in range(n): #그래프 구성
        graph.append(list(map(int,sys.stdin.readline().split())))
    
    priorQue = []
    heapq.heappush(priorQue,(graph[0][0],0,0))#시작점 방문
    
    while priorQue:
        dist,x,y = heapq.heappop(priorQue)

        if(minDist[x][y]>dist):
            minDist[x][y] = dist # 최소 비용 갱신
            
            for go in range(4):
                nextX = x+dx[go]
                nextY = y+dy[go]
                if(chkXY(nextX) and chkXY(nextY)):#이동 가능한 곳
                    heapq.heappush(priorQue,(graph[nextX][nextY]+dist,nextX,nextY)) # 우선 순위 큐 삽입
    

    print(minDist[n-1][n-1])








