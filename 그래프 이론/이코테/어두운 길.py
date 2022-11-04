import sys

n,m = map(int,sys.stdin.readline().split())


rootv = [i for i in range(n)]

eL = []

for _ in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    eL.append((z,x,y))

eL.sort() #정렬

def findRoot(rootv,v):
    if(rootv[v]!=v):
        rootv[v] = findRoot(rootv,rootv[v])
    return rootv[v]

def union(rootv,v1,v2):
    rootV1 = findRoot(rootv,v1)
    rootV2 = findRoot(rootv,v2)
    isCost = False # 돈이 드는지 안드는지 여부

    if(rootV1!=rootV2): #길 이어줌
        if(rootV2>rootV1):
            rootv[rootV2] = rootV1
        else:
            rootv[rootV1] = rootV2
        isCost = True #돈 듬

    return isCost
    

toalcost = 0
realcost =0
for z,x,y in eL:
    toalcost+=z
    if(union(rootv,x,y)):# 길이 이어지면
        realcost += z # 비용 추가
        

print(toalcost-realcost) #최대 아끼게 된 돈

    





