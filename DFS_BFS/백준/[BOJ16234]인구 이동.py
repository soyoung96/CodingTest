import sys
from collections import deque
from copy import deepcopy
from pprint import pprint

n,l,r = map(int,sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

count = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def checkXY(xy):
    if(0<=xy<n):
        return True
    else:
        return False


while(True):
    visited = set([]) #국경선 열린 동네
    peoplemove = False #인구 이동 False
    graph2 = deepcopy(graph) #2500
    for x in range(n):
        for y in range(n): #2500*2500
            if( (x,y) not in visited):
                nowvisitied = []
                visitedNum =0 #국경선 열린 동네 수
                visitedSum = 0 #국경선 열린 동네 인구 합친 수
                que = deque([])
                que.append((x,y))
                visitedNum+=1
                visitedSum+=graph[x][y]
                visited.add((x,y))
                nowvisitied.append((x,y))
                while(que): #bfs #2500
                    nowX,nowY = que.popleft()
                    # print(nowX, nowY)
                    for go in range(4):
                        nextX,nextY = nowX+dx[go],nowY+dy[go]
                        
                        if(checkXY(nextX) and checkXY(nextY) and ((nextX,nextY) not in visited)): #갈 수 있고, 방문한 적이 없다면
                            nextPeopleNum = graph[nextX][nextY]
                            nowPeolpleNum = graph[nowX][nowY]
                            if(l<=abs(nowPeolpleNum - nextPeopleNum)<=r):#두 나라의 인구 차이가 L명 이상, R명 이하라면
                                peoplemove = True #인구 이동이 일어났으므로
                                que.append((nextX,nextY))
                                visitedNum+=1
                                visitedSum+=nextPeopleNum
                                visited.add((nextX,nextY))
                                nowvisitied.append((nextX,nextY))
                sharePeople = visitedSum//visitedNum #소수점 버림
                for x_,y_ in nowvisitied: #2500 #for문 안에 같은 x,y 변수 실수 주의
                    graph2[x_][y_] = sharePeople
    # print(peoplemove)                
    if(not peoplemove):
        break #탈출
    else:
        count+=1 #인구이동한 턴 증가
        graph = graph2
        # pprint(graph)
        # if(count==5):
        #     break


print(count)

                
# import sys
# from collections import deque
# from copy import deepcopy
# from pprint import pprint

# n,l,r = map(int,sys.stdin.readline().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int,sys.stdin.readline().split())))

# count = 0

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# def checkXY(xy):
#     if(0<=xy<n):
#         return True
#     else:
#         return False


# while(True):
#     unions = [[-1]*(n) for _ in range(n)]
#     graph2 = deepcopy(graph) #2500
#     union = 1
#     for x in range(n):
#         for y in range(n): #2500*2500
#             if(unions[x][y] == -1):
#                 nowvisitied = []
#                 # visitedNum =0 #국경선 열린 동네 수
#                 # visitedSum = 0 #국경선 열린 동네 인구 합친 수
#                 que = deque()
#                 que.append((x,y))
#                 visitedNum=1#국경선 열린 동네 수
#                 visitedSum=graph[x][y]#국경선 열린 동네 인구 합친 수
#                 nowvisitied.append((x,y))
#                 unions[x][y] = union
#                 while(que): #bfs #2500
#                     nowX,nowY = que.popleft()
#                     # print(nowX, nowY)
#                     for go in range(4):
#                         nextX,nextY = nowX+dx[go],nowY+dy[go]
                        
#                         if(checkXY(nextX) and checkXY(nextY) and unions[nextX][nextY] == -1): #갈 수 있고, 방문한 적이 없다면
#                             # print(nextX,nextY)
#                             nextPeopleNum = graph[nextX][nextY]
#                             nowPeolpleNum = graph[nowX][nowY]
#                             if(l<=abs(nowPeolpleNum - nextPeopleNum)<=r):#두 나라의 인구 차이가 L명 이상, R명 이하라면
#                                 que.append((nextX,nextY))
#                                 visitedNum+=1
#                                 visitedSum+=nextPeopleNum
#                                 nowvisitied.append((nextX,nextY))
#                                 unions[nextX][nextY] = union
#                             # pprint(unions)
#                 # sharePeople = visitedSum//visitedNum #소수점 버림
#                 for x_,y_ in nowvisitied: #2500
#                     graph2[x_][y_] = visitedSum//visitedNum #소수점 버림
#                 union+=1
#     # print(peoplemove)                
#     if(union == n*n+1):
#         break #탈출
#     else:
#         count+=1 #인구이동한 턴 증가
#         graph = graph2
#         # pprint(graph)
#         # if(count==5):
#         #     break


# print(count)

                






                    



            






                    



            
