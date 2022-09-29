import sys

n,m,k = map(int,sys.stdin.readline().rstrip().split())
inputL = sorted(list(map(int,sys.stdin.readline().rstrip().split())),reverse=True) #O(nlogn)

answer=0

first=inputL[0]
second=inputL[1]

expNum=0

for _ in range(m):#O(10000)
    for _ in range(k):#O(10000)
        answer+=first
        expNum+=1
        if(m==expNum):
            break
    if(m==expNum):
        break
    else:
        answer+=second
        expNum+=1
        if(m==expNum):
            break


print("{0}".format(answer))




