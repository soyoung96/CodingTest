import sys


import sys

dx=[-1,1,0,0]#상하좌우
dy=[0,0,-1,1]

n =int(sys.stdin.readline())

array=list(sys.stdin.readline().rstrip().split())


mapL = [[0]*(n+1) for _ in range(n+1)]

x,y=(1,1)

UDLR=['U','D','L','R']
for go in array: #O(100)
    for i in range(4): #상하좌우
        if(go ==UDLR[i]):
            nextX = x+dx[i]
            nextY = y+dy[i]
            if(nextX==0 or nextX>n or nextY==0 or nextY>n):#못감
                continue
            else:
                x = nextX
                y = nextY

print("{0} {1}".format(x,y))