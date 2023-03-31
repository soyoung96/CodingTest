import sys

sys.setrecursionlimit(int(1e5))
r,c = map(int,sys.stdin.readline().split())

graph = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]


for _ in range(r):
    inputL = list(sys.stdin.readline().rstrip())
    graph.append(inputL)


def chkX(x,c):
    if(0<=x<c):
        return True
    else:
        return False

def chkY(y,r):
    if(0<=y<r):
        return True
    else:
        return False
maxStep = 0
dpL = [0 for _ in range(26)]
def dfs(y,x,step):
    global maxStep
    # print(y,x)
    alpha = graph[y][x]
    dpL[ord(alpha)-ord('A')] = 1
    step +=1
    if(maxStep<step):
        maxStep = step
    for go in range(4):
        newX = x+dx[go]
        newY = y+dy[go]
        if(chkX(newX,c) and chkY(newY,r)): 
            if(dpL[ord(graph[newY][newX])-ord('A')] == 0): #방문한 적 없는 알파벳
                dfs(newY,newX,step)
    dpL[ord(alpha)-ord('A')] = 0
    # pprint(dpGraph)
    
dfs(0,0,0)
print(maxStep)
        