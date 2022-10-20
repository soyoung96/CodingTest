import sys
from pprint import pprint

t = int(sys.stdin.readline())

dx = [1,0,-1]
dy = [-1,-1,-1] # 왼아래, 왼,왼위

def checkX(x):
    if(0<=x<n):
        return True
    else:
        return False

def checkY(y):
    if(0<=y<m):
        return True
    else:
        return False
    

for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())

    dp = [[-1]*m for _ in range(n)]
    inputMat = []
    inputArray = list(map(int,sys.stdin.readline().split()))

    for x in range(n):
        inputMat.append(inputArray[x*m:x*m+m])

    for x in range(n):#첫 열은 그냥 dp 기록
        dp[x][0] = inputMat[x][0]

    for y in range(1,m):
        for x in range(n):
            maxList=[] # 최댓값의 후보가 있는 공간
            for move in range(3):
                nextX,nextY = x+dx[move], y+dy[move]
                if(checkX(nextX) and checkY(nextY)): #갈 수 있는 곳이라면
                    maxList.append(dp[nextX][nextY])
            
            dp[x][y] = inputMat[x][y]+max(maxList)
    
    answer = -1
    for i in range(n):#마지막 열 순회하면서 최댓값 구함
        if(dp[i][m-1]>answer):
            answer =dp[i][m-1]

    print(answer)





    
    
