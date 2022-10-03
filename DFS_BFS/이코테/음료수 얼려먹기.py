from pprint import pprint
from re import L
import sys

n,m = map(int,sys.stdin.readline().split())

mapL=[]

# for _ in range(n):
#     mapL.append([int(i) for i in list(sys.stdin.readline().rstrip())])

for _ in range(n):
    mapL.append(list(map(int,sys.stdin.readline().rstrip())))
    #input() 아닌 sys.stdin.readline()로 연속된 str 받아줄 때 rstirp 잊지 말것

dx=[1,-1,0,0]
dy=[0,0,-1,1]

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

def dfs(x,y,list):
    list[x][y]=2 #첫노드 방문
    for i in range(4):
        nextX=x+dx[i]
        nextY=y+dy[i]
        if(chkX(nextX) and chkY(nextY)): #해당 칸으로 이동은 가능
            if(list[nextX][nextY]==0):#가본 곳 아니고!=2, 공간이 있다면!=1
                dfs(nextX,nextY,list)

answer=0
for x in range(n):
    for y in range(m):#1000*1000
        if(mapL[x][y]==0):
            answer+=1
            dfs(x,y,mapL)

print(answer)


