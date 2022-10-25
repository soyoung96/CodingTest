import sys
from itertools import combinations
import copy
from collections import deque

from pprint import pprint 

comArr = []

badArr=[]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


n,m = map(int,sys.stdin.readline().split())

def chkX(x):
    if(1<=x<=n):
        return True
    else:
        return False

def chkY(y):
    if(1<=y<=m):
        return True
    else:
        return False

inputMat = [[0] * (m+1)]

for _ in range(n):
    inputArr = [0]
    inputArr.extend(list(map(int,sys.stdin.readline().split())))
    inputMat.append(inputArr)

for x in range(1,n+1):
    for y in range(1,m+1):
        if(inputMat[x][y] == 2):
            badArr.append((x,y))
        if(inputMat[x][y] == 0):
            comArr.append((x,y))

comArr = list(combinations(comArr,3)) #O(n^3) -> n==64

answer = -1
for elt in comArr:
    tmpInputMat = copy.deepcopy(inputMat)
    tmpAnswer = 0
    
    for comX,comY in elt:# 벽 3개 세우기
        tmpInputMat[comX][comY] = 1
    
    for badX,badY in badArr: #BFS O(n^2)
        q = deque([])
        q.append((badX,badY))
        while q:
            badX,badY = q.popleft()
            for i in range(4):
                nextBadX = badX+dx[i]
                nextBadY = badY+dy[i]
                if(chkX(nextBadX)and chkY(nextBadY)): #이동할 수 있으면
                    if(tmpInputMat[nextBadX][nextBadY] == 0): #빈칸이라면
                        tmpInputMat[nextBadX][nextBadY] = 2 #오염
                        q.append((nextBadX,nextBadY))
    
    for x in range(1,n+1): #빈칸 갯수 세기
        for y in range(1,m+1):
            if(tmpInputMat[x][y] == 0):
                tmpAnswer+=1
    
    if(answer<tmpAnswer): #빈칸이 최대인 답 구하기
        answer = tmpAnswer

print(answer)







    

    







