import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

dx =[1,-1,0,0]
dy =[0,0,-1,1] #남,북,서,동

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

mapL=[]
stepL = [[0]*m for i in range(n)]
for _ in range(n):
    mapL.append(list(map(int,sys.stdin.readline().rstrip())))

x,y = 0,0 #현재 위치

mapL[x][y] = 2 # 방문
stepL[x][y] = 1
queue = deque([(x,y)])

while queue: #O(n**2)
    x,y=queue.popleft()
    for i in range(4):
        nextX = x+dx[i]
        nextY = y + dy[i]
        if(chkX(nextX) and chkY(nextY)):
            if(mapL[nextX][nextY] == 1): #방문하지 않았고, 괴물 없는 상태
                mapL[nextX][nextY] = 2 # 방문
                stepL[nextX][nextY] = stepL[x][y]+1
                queue.append((nextX,nextY))

print(stepL[n-1][m-1])



    

