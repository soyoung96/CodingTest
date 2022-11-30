import sys

n = int(sys.stdin.readline())

inputL = []
for _ in range(n):
    inputL.append(list(map(int,sys.stdin.readline().split())))


inputL.sort()

preS = inputL[0][0]
preE = inputL[0][1]
minusTotal = 0
for ind in range(1,len(inputL)):
    newS = inputL[ind][0]
    newE = inputL[ind][1]
    if(preE<newS):
        minusTotal+= (newS - preE)
    
    preE = max(preE,newE)

print(preE-preS-minusTotal)


