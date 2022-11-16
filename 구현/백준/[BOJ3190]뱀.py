import sys
from collections import deque
from pprint import pprint


n = int(sys.stdin.readline())

k =  int(sys.stdin.readline())

dx = [0,1,0,-1]
dy = [1,0,-1,0] #시계방향

def fixGo(go): #방향 픽스
    if(go<0):
        go = 3
    return go%4

graph=[[0]* n for _ in range(n)]

for _ in range(k):
    x,y = map(int,sys.stdin.readline().split())
    graph[x-1][y-1] = 1

l =  int(sys.stdin.readline())

goL = deque([])
for _ in range(l):
    x,c = sys.stdin.readline().rstrip().split()
    x = int(x)
    goL.append((x,c))


count = 0

head=[0,0]
tail=[0,0]
graph[0][0] = 2 #뱀 위치 2~5 -> 오른쪽 부터 시계 방향

go = 0# 처음 오른쪽

def chkXY(x):
    if(0<=x<n):
        return True
    else:
        return False
while(True):

    if(goL and goL[0][0] == count ):# 디큐 비지 않았고,방향 바꿀 시간 됌
        _,c = goL.popleft()
        if(c == "D"):
            c=1
        else:
            c=-1
        go = fixGo(go+c) #방향 갱신
        graph[head[0]][head[1]] = go+2 #머리 방향 갱신
       
    nextX = head[0]+dx[go]
    nextY = head[1]+ dy[go]
    if(chkXY(nextX) and chkXY(nextY)): #이동 가능
        if(2<=graph[nextX][nextY]<6):#꼬리밟음
            count+=1 #이동해서 자기 밟고
            break
        elif(graph[nextX][nextY]==1): #사과
            graph[nextX][nextY]=go+2 #먹어서 자기 존재
            head = [nextX,nextY] #머리 이동
        else: #빈칸
            graph[nextX][nextY]=go+2 #자기 존재
            tailGo = graph[tail[0]][tail[1]]-2 #다음 꼬리 방향
            nextTail = [tail[0]+dx[tailGo],tail[1]+dy[tailGo]] #다음 꼬리 위치
            graph[tail[0]][tail[1]] = 0 #현재 꼬리 빈칸
            tail = nextTail #꼬리 다음 꼬리로 이동
            head = [nextX,nextY] #머리 이동
        
        count+=1


    else:
        count+=1 #벽으로 이동하고
        break
    # pprint(graph)
    # print(tail)
    # print()


print(count)
