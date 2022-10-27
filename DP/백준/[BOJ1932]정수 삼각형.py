import sys

dx = [1,1]
dy = [1,0]
n = int(sys.stdin.readline())
inputL = []

for _ in range(n):
    inputL.append(list(map(int,sys.stdin.readline().split())))


answer = -1
if(n>1):
    for x in range(n-2,-1,-1):
        for y in range(len(inputL[x])):
            inputL[x][y] = inputL[x][y] + max(inputL[x+dx[0]][y+dy[0]],inputL[x+dx[1]][y+dy[1]])


print(inputL[0][0])
    




