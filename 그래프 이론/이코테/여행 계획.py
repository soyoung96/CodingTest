import sys

n,m = map(int,sys.stdin.readline().split()) # n,m 각각 500

rootL = [i for i in range(n+1)]

inputMat = [[0]*(n+1)]

for _ in range(n):
    inputList = [0]
    inputList.extend(list(map(int,sys.stdin.readline().split())))
    inputMat.append(inputList)

chkNode = list(map(int,sys.stdin.readline().split()))# 여기의 루트노드가 모두 같아야 함

def findRoot(rootL,a): #a의 루트를 찾음 O(n)
    if(rootL[a]!=a):
        rootL[a] = findRoot(rootL,rootL[a])
    return rootL[a]

def unionNode(inputMat,rootL):#(n^3) -> n =500이라 OK
    for x in range(1,n+1):
        for y in range(1,n+1): #O(n^2)
            if(inputMat[x][y] == 1):
                rootX = findRoot(rootL,x)#O(n)
                rootY = findRoot(rootL,y)
                if(rootX != rootY): #루트가 서로 같지 않다면 합쳐줌
                    if(rootX>rootY):
                        rootL[x] = rootY
                    else:
                        rootL[y] = rootX

unionNode(inputMat,rootL)

answer = "YES"


for ind in range(1,len(chkNode)):
    if(rootL[chkNode[0]]!=rootL[chkNode[ind]]): #하나라도 다른 루트노드 있으면
        answer ="NO"

print(answer)



    
                    
