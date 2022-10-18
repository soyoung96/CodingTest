import sys

def findRoot(rootL,a):
    if(rootL[a] != a):
        rootL[a] = findRoot(rootL,rootL[a]) #루트 갱신
    
    return rootL[a]

def unionNode(rootL,a,b):
    rootA = findRoot(rootL,a)
    rootB = findRoot(rootL,b)
    if(rootA != rootB):
        if(rootA<rootB):
            rootL[rootB] = rootA
        else:
            rootL[rootA] = rootB
        return True
    else: #이미 같은 신장트리
        return False

n,m = map(int,sys.stdin.readline().split())

rootL = [i for i in range(n+1)]
inputL = []

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    inputL.append((c,a,b))

inputL.sort() #모든 간선 비용 오름차순에 따라 정렬

maxCost=0
totalCost = 0
for cost,start,end in inputL:
    if(unionNode(rootL,start,end)): #같은 신장 트리가 아닐때
        
        totalCost+=cost
        maxCost = cost



print(totalCost - maxCost)


