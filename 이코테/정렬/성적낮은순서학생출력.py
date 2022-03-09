n = int(input())
inputL=[]

for i in range(n):
  name,score=input().split()
  score = int(score)
  inputL.append([name,score])

inputL = sorted(inputL,key = lambda x:x[1])

for i in inputL:
  print(i[0], end=" ")
