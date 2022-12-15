import sys

n = int(sys.stdin.readline())

inputL = list(map(int,sys.stdin.readline().split()))

inputLPlusIndex = []
for ind in range(n):#1000000
    inputLPlusIndex.append((inputL[ind],ind))

inputLPlusIndex.sort() #1000000log1000000

answer = [-1 for _ in range(n)]

preInputLVal = -1
sameCount =0
for val,(inputLVal,ind) in enumerate(inputLPlusIndex): #1000000
    if(preInputLVal == inputLVal):
        sameCount+=1
    answer[ind] = val - sameCount
    preInputLVal = inputLVal

for elt in answer:#1000000
    print(elt,end = " ")
    
    
