import sys

n,m = map(int,sys.stdin.readline().split())

inputL = list(map(int,sys.stdin.readline().split()))

def getTree(inputL,height): #O(1000000) #height 길이의 절단기로 얻을 수 있는 나무양 
    sum = 0
    for inputE in inputL:
        sum+=(max(inputE - height,0))
    return sum

rightH = max(inputL)#칼의 최대길이 #O(1000000)
leftH = 0#칼의 최소길이

maxAnswer = -1
while(leftH <= rightH): #O(1000000log2000000000)
    midH = (leftH+rightH)//2
    
    tree = getTree(inputL,midH)

    if(tree<m): #절단기 높이 줄여야함
        rightH = midH-1
    else: #절단기 높이 높여도 된다
        if(maxAnswer<midH):
            maxAnswer = midH
        leftH = midH+1


print(maxAnswer)






        

