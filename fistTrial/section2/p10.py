n = int(input())
result = list(map(int,input().split()))

score=0
subScore=0
for i in range(n):
  if(result[i]==1):
    subScore+=1
    score+=subScore
  else:
    subScore=0

print(score)