n = int(input())
axisList =list()

sumList=list()

for i in range(n):
  tmpList = list(map(int,input().split()))
  axisList.append(tmpList)

for x in range(n):
  tmpSum=0
  for y in range(n):
    tmpSum+=axisList[y][x]
  sumList.append(tmpSum)

for y in range(n):
  tmpSum=0
  for x in range(n):
    tmpSum+=axisList[y][x]
  sumList.append(tmpSum)

tmpSum=0
for m in range(n):
  tmpSum+=axisList[m][m]
sumList.append(tmpSum)

tmpSum=0
for m in range(n):
  tmpSum+=axisList[m][n-m-1]
sumList.append(tmpSum)


print(sorted(sumList)[-1])
  
  