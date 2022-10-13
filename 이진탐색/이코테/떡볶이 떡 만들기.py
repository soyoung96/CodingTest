import sys

n,m = map(int,sys.stdin.readline().split())
inputL = list(map(int,sys.stdin.readline().split()))

start=0
end= max(inputL)

def getLength(height): #O(10^6) #떡 길이 구함
    global inputL
    length=0
    for elt in inputL:
        eltLength = elt - height
        if(eltLength>0):
            length+=eltLength
    return length

maxH=-1
while start<=end:
    mid= (start + end)//2
    length = getLength(mid)
    if(m==length):
        maxH = mid
        break
    elif(m>getLength(mid)): #h를 줄여야 한다
        end= mid-1
    else: #h를 늘릴 수 있다.
        maxH = mid
        start = mid+1

print(maxH)
        
