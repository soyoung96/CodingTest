import sys

n = int(sys.stdin.readline())

inputL=[]
for _ in range(n):
    name,score = sys.stdin.readline().split()
    inputL.append((name,int(score)))

inputL.sort(key=lambda x:x[1])


for i in range(n):
    print(inputL[i][0],end=" ")