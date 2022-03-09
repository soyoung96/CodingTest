# n = int(input())
# totalList=list()
# for i in range(n):
#   if(i == 0):
#     tmp = [0]*(n+2)
#     totalList.append(tmp)
#   tmp = [0]+list(map(int,input().split()))+[0]
#   totalList.append(tmp)
#   if(i == n-1):
#     tmp = [0]*(n+2)
#     totalList.append(tmp)

# cnt=0
# for y in range(1,n+1):
#   for x in range(1,n+1):
#     me = totalList[y][x]
#     r = totalList[y][x+1]
#     l = totalList[y][x-1]
#     u = totalList[y-1][x]
#     d = totalList[y+1][x]
#     if(((me>r and me>l)and me>u) and me>d):
#       cnt+=1

# print(cnt)

n = int(input())
totalList=[list(map(int,input().split())) for _ in range(n)]

dx=[0,1,0,-1]
dy=[-1,0,1,0]

totalList.insert(0,[0]*n)
totalList.append([0]*n)
for a in totalList:
  a.append(0)
  a.insert(0,0)

cnt=0
for y in range(1,n+1):
  for x in range(1,n+1):
    if(all(totalList[y][x]> totalList[y+dy[i]][x+dx[i]] for i in range(4))):
      cnt+=1

print(cnt)
  
    
    