import sys

n = int(sys.stdin.readline())
inputL = []
for _ in range(n):
    inputL.append(int(sys.stdin.readline()))

for i in sorted(inputL,reverse=True):
    print(i,end=" ")
