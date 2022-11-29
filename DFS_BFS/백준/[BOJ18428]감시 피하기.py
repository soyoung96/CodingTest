# import sys

# n = int(sys.stdin.readline())

# dx=[0,0,-1,1]
# dy=[1,-1,0,0]

# def chkXY(xy):
#     if(0<=xy<n):
#         return True
#     else:
#         return False

# graph = []

# for _ in range(n):
#     graph.append(list(sys.stdin.readline().rstrip().split()))

# answer = ""
# totalJ=0
# for x in range(n):
#     for y in range(n):
#         if(graph[x][y] == "T"):
#             for go in range(4): #4방향
#                 nextX = x+dx[go]
#                 nextY = y+dy[go]
#                 while(chkXY(nextX) and chkXY(nextY)): #갈 수 있다면
#                     if(graph[nextX][nextY]=="J"):#갔는데 장애물
#                         break
#                     if(graph[nextX][nextY] == "S"): #갔는데 학생
#                         preX = x-dx[go]
#                         preY = y -dx[go]
#                         if(preX==x and preY==y): #선생자리
#                             answer = "NO"
#                             break
#                         elif(totalJ>=3):# 더이상 장애물 설치 불가
#                             answer = "NO"
#                             break
#                         else:# 장애물 설치
#                             graph[preX][preY]


#                 if(answer=="NO"):
#                     break

#             if(answer=="NO"):
#                 break
#     if(answer=="NO"):
#                 break


import sys
from itertools import combinations
import copy
from pprint import pprint

n = int(sys.stdin.readline())

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def chkXY(xy):
    if(0<=xy<n):
        return True
    else:
        return False

graph = []

tmpComb = []

for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip().split()))

for x in range(n):
    for y in range(n):
        if(graph[x][y] == "X"): #빈칸
            tmpComb.append([x,y])

answerF = "NO"
for f,s,t in combinations(tmpComb,3): #6*35*34*36 -> 상관 무
    tmpGraph = copy.deepcopy(graph)
    tmpGraph[f[0]][f[1]] = "J"
    tmpGraph[s[0]][s[1]] = "J"
    tmpGraph[t[0]][t[1]] = "J"
    answer="YES"

    for x in range(n):
        for y in range(n):
            if(tmpGraph[x][y] == "T"):
                for go in range(4): #4방향
                    nextX = x+dx[go]
                    nextY = y+dy[go]
                    while(chkXY(nextX) and chkXY(nextY)): #갈 수 있다면
                        if(tmpGraph[nextX][nextY] == "J"): #갔는데 장애물
                            break
                        if(tmpGraph[nextX][nextY] == "S"): #갔는데 학생
                            answer="NO"
                            break
                        nextX = nextX+dx[go]
                        nextY = nextY+dy[go]
                    if(answer=="NO"):
                        break
                if(answer == "NO"):
                    break
        if(answer=="NO"):
            break
    if(answer == "YES"):
        answerF = "YES"
        break

print(answerF)           



