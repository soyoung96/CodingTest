import sys
from collections  import deque
from pprint import pprint

n = int(sys.stdin.readline())

mapL = []


for _ in range(n):
    mapL.append(list(map(int,sys.stdin.readline().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def chkXY(xy):
    if(0<=xy<n):
        return True
    else:
        return False


maxTotalSum = -1

for h in range(101):
    waterMap = [[0]*n for _ in range(n)]
    totalSum = 0
    for x in range(n):
        for y in range(n): #1000000
            if(waterMap[x][y] == 0 and h<mapL[x][y]): #방문 안했고 높으면 살아남음
                que =deque([])
                que.append((x,y))
                waterMap[x][y] = 1
                totalSum+=1
                while(que):
                    preX,preY = que.popleft()
                    for go in range(4):
                        nextX = preX+dx[go]
                        nextY = preY+dy[go]
                        if(chkXY(nextX) and chkXY(nextY) and waterMap[nextX][nextY] == 0):
                            if(h<mapL[nextX][nextY]):
                                waterMap[nextX][nextY] = 1
                                que.append((nextX,nextY))

    if(maxTotalSum<totalSum):
        maxTotalSum = totalSum

print(maxTotalSum)
                


