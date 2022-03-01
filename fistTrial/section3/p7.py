# n = int(input())

# inputList = [list(map(int,input().split())) for _ in range(n)]

# midInd = (n+1)//2
# appleSum = 0
# step=0
# for y in range(n):
#   if((2*y+1)<=n):
#     step+=1
#     appleSum+=sum(inputList[y][midInd-step:midInd-1+step])
#   else:
#     step-=1
#     appleSum+=sum(inputList[y][midInd-step:midInd-1+step])

# print(appleSum)

'''
이런 문제는 s point와 e point 생각해낼 것
'''

n = int(input())

inputList = [list(map(int,input().split())) for _ in range(n)]

s = n//2
e = n//2 +1
appleSum = 0
for y in range(n):
  for x in range(s,e):
    appleSum+=inputList[y][x]
  if(y<(n//2)):
    s-=1
    e+=1
  else:
    s+=1
    e-=1
  
  
print(appleSum)