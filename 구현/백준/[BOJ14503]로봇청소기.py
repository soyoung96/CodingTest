import sys


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

def defineD(d):
    if(d<0):
        return 4+d
    else:
        return d

n,m = map(int,sys.stdin.readline().split())

r,c,d = map(int,sys.stdin.readline().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1] #북동남서

graph = []

for _ in range(n):
    inputL = list(map(int,sys.stdin.readline().split()))
    graph.append(inputL)

ans = 0 #청소한 칸의 수


graph[r][c] = 2#청소
ans+=1#청소한 칸의 수 증가

while(True):
    go = False
    for _ in range(4):
        d = defineD(d-1) #왼쪽으로 방향 갱신
        newR = r+dx[d]
        newC = c+dy[d]
        if(chkX(newR) and chkY(newC)): #그래프내의
            if(graph[newR][newC]==0): #청소안한 빈칸
                r = newR
                c = newC #rc갱신
                graph[r][c] = 2#청소
                ans+=1#청소한 칸의 수 증가
                go = True #움직임
                break
    if(go):
        continue
    else: #네 방향 모두 청소가 이미 되어있거나 벽인 경우
        newR = r+dx[defineD(d-2)]
        newC = c+dy[defineD(d-2)]
        if(chkX(newR) and chkY(newC)): #그래프내의
            if(graph[newR][newC]==2): #청소한 빈칸
                r = newR
                c = newC #rc갱신
                continue
        
        break #그래프내가 아니거나 그래프내의 벽이라면


print(ans)










