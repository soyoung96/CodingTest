import sys

n,k = map(int,sys.stdin.readline().split())

inputL=[]
for _ in range(2):
    inputL.append(list(map(int,sys.stdin.readline().split())))

A = inputL[0]
B = inputL[1]

A.sort()
B.sort(reverse=True)

for i in range(k):
    A[i],B[i] = B[i],A[i]

print(sum(A))
