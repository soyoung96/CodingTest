import sys

n = int(sys.stdin.readline())

inputL = list(map(int,sys.stdin.readline().split()))

mostLike0 = int(1e10)

leftP = 0
rightP = len(inputL)-1

ansLeftP = -1
ansRightP = -1
while(leftP<rightP):#O(100000)
    # print(ansLeftP,ansRightP)
    leftN = inputL[leftP] #용액농도1
    rightN = inputL[rightP]#용액농도2
    resultN= rightN + leftN #두 용액 섞은 농도의 절댓값
    # print(resultN)
    if(mostLike0>abs(resultN)):
        mostLike0 = abs(resultN)
        ansLeftP = leftP
        ansRightP = rightP
        if(mostLike0 == 0):
            break
    if(resultN>0):
        rightP-=1
    else:
        leftP+=1

print(inputL[ansLeftP],inputL[ansRightP])   
