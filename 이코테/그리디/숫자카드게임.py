n,m = map(int,input().split())
inputL =[list(map(int,input().split())) for _ in range(n)]
minL=[100000]*n

for i in range(n):
  for j in range(m):
    if(inputL[i][j]<minL[i]):
      minL[i] = inputL[i][j]

print(sorted(minL)[-1])