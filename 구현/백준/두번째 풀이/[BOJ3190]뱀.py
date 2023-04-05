import sys
from collections import deque
from pprint import pprint
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

dx = [0,1,0,-1]
dy = [1,0,-1,0] # 뱀머리 오른쪽에서 시계방향(오른쪽 D로)회전 순

graph = [[-1] * (n+1) for _ in range(n+1)]

for _ in range(k):
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = -2 #사과 투척
l = int(sys.stdin.readline())

moveL = deque([])
for _ in range(l):
    x,c = sys.stdin.readline().rstrip().split()
    x = int(x)
    moveL.append((x,c))

nowX = 1
nowY = 1

tailX = 1
tailY = 1

go = 0
graph[nowX][nowY] = go

s = 0

def chGo(go,c):
    if(c=='D'):
        return (go+1)%4
    else:
        return (go-1)%4

def chkXY(xy):
    if(1<=xy<=n):
        return True
    else:
        return False

while(True):

    if(moveL):
        if(moveL[0][0] == s):
            _,c = moveL.popleft()
            go = chGo(go,c)
            graph[nowX][nowY] = go #머리 위치만 변경

    nowX += dx[go]
    nowY += dy[go]

    if(chkXY(nowX) and chkXY(nowY)):
        if(graph[nowX][nowY] == -2): #사과 있다
            graph[nowX][nowY] = go #머리 위치만 변경
        elif(0<=graph[nowX][nowY]<=3): #자기 몸이랑 부딫힘
            break
        else: #사과없다
            graph[nowX][nowY] = go #머리 위치만 변경
            tailGo = graph[tailX][tailY] #비워줌
            graph[tailX][tailY] = -1 # 비워줌
            tailX += dx[tailGo]
            tailY += dy[tailGo]

    else: #벽이랑 부딫힘
        break
    s+=1
    # pprint(graph)

    
print(s+1)










