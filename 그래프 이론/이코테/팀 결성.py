import sys

n,m = map(int,sys.stdin.readline().split())

rootL = [0] * (n+1)

for i in range(1,n+1):
    rootL[i] = i

def findRoot(rootL,node): #해당 노드의 root 찾음
    if(rootL[node] != node):
        rootL[node] = findRoot(rootL,rootL[node])

    return rootL[node]

def unionteam(rootL,a,b):
    rootA = findRoot(rootL,a)
    rootB = findRoot(rootL,b)
    if(rootA <rootB):
        rootL[b] = rootA
    else:
        rootL[a] = rootB


for _ in range(m):
    exp,a,b = map(int,sys.stdin.readline().split())
    if(exp ==0):# 팀 합치기
        unionteam(rootL,a,b)
    
    else: #같은 팀 여부 확인
        rootA = findRoot(rootL,a)
        rootB = findRoot(rootL,b)
        if(rootA == rootB): #r같은 팀
            print("YES")
        else: # 다른팀
            print("NO")


