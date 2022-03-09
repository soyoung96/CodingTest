# n = int(input())
# inputList=[list(map(int,input().split())) for _ in range(n)]

# m = int(input())
# turnList = [list(map(int,input().split())) for _ in range(m)]

# for i in range(m):
#   y = turnList[i][0]
#   to = turnList[i][1]
#   step = turnList[i][2]

#   if(to ==0):
#     tmpList = inputList[y-1][:step]
#     inputList[y-1][:n-step] = inputList[y-1][step:]
#     inputList[y-1][n-step:] = tmpList
#   else:
#     tmpList = inputList[y-1][n-step:]
#     inputList[y-1][step:] = inputList[y-1][:n-step]
#     inputList[y-1][:step] = tmpList

# s = 0
# e = n
# sum =0
# for y in range(n):
#   for x in range(s,e): #range or 인덱싱[:]시 마지막 주의
#     sum += inputList[y][x]
#   if(y<n//2): #하드코딩 주의!!!!!!
#     s+=1
#     e-=1
#   else:
#     s-=1
#     e+=1

# print(sum)


n = int(input())
inputList=[list(map(int,input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
  y,to,step=map(int,input().split())
  for j in range(step):
    if(to==0):
      inputList[y-1].append(inputList[y-1].pop(0))
    else:
      inputList[y-1].insert(0,inputList[y-1].pop())
    

s = 0
e = n
sum =0
for y in range(n):
  for x in range(s,e): #range or 인덱싱[:]시 마지막 주의
    sum += inputList[y][x]
  if(y<n//2): #하드코딩 주의!!!!!!
    s+=1
    e-=1
  else:
    s-=1
    e+=1

print(sum)
