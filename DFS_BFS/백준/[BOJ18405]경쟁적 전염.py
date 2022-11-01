import sys
from collections import deque
from pprint import pprint

n,k = map(int,sys.stdin.readline().split())

inputL = [[-1] *(n+1)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def chkXY(x):
    if(1<=x<=n):
        return True
    else:
        return False

for _ in range(n):
    inputLTmp = [-1]
    inputLTmp.extend(list(map(int,sys.stdin.readline().split())))

    inputL.append(inputLTmp)

bugQue = []

for x in range(1,n+1):
    for y in range(1,n+1):
        if(inputL[x][y] !=0): #바이러스 자리일때
            bugQue.append([x,y,inputL[x][y],0])

bugQue.sort(key= lambda x:x[2]) #우선순위 높은 순 정렬

bugQue = deque(bugQue) #큐전환

s,x,y = map(int,sys.stdin.readline().split())


def nextDFS(inputL,bugQue,n,s):

    while(bugQue):
        x,y,k,t = bugQue.popleft()
        if(t==s): #초가 다되면
            break
        for go in range(4): #4가지 방향으로
            nextX = x+ dx[go]
            nextY = y+ dy[go]

            if(chkXY(nextX) and chkXY(nextY)): #이동가능한 자리면
                if(inputL[nextX][nextY] == 0): #빈자리면
                    inputL[nextX][nextY] = k #오염
                    bugQue.append([nextX,nextY,k,t+1]) #큐 삽입

nextDFS(inputL,bugQue,n,s)

print(inputL[x][y])

            








