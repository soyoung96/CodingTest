# n,m = map(int,input().split())
# y,x,way=map(int,input().split())
# inputL = [list(map(int,input().split())) for _ in range(n)]
# #북동남서
# dx=[0,1,0,-1]
# dy=[-1,0,1,0]

# turnL=[3,0,1,2]
# turnB=[2,3,0,1]
# cnt=0
# noway=0
# while(True):
#   if(inputL[y][x]==0):
#     inputL[y][x]=-1#갔음
#     cnt+=1
#   way=turnL[way] #왼쪽으로 돌았
#   tmpY,tmpX = y+dy[way],x+dx[way]
#   if(inputL[tmpY][tmpX]!=0): #안가본데 아님
#     noway+=1
#     if(noway==4):#4번돌았
#       tmpY,tmpX = y+dy[turnB[way]],x+dx[turnB[way]] #뒤돌아
#       if(inputL[tmpY][tmpX]==1):#바다일때
#         break
#       else:
#         y,x =tmpY,tmpX#이동
#         noway=0
#         continue#1단계로 돌아감
#     else:#아직 4번 안돌
#       continue#1단계로 돌아감
#   else: #안가본데
#     y,x =tmpY,tmpX
#     noway=0

# print(cnt)

n,m = map(int,input().split())
y,x,way=map(int,input().split())
inputL = [list(map(int,input().split())) for _ in range(n)]
#북동남서
dx=[0,1,0,-1]
dy=[-1,0,1,0]

turnL=[3,0,1,2]
turnB=[2,3,0,1]

noway=0
inputL[y][x]=-1#갔음
cnt=1
while(True):
  way=turnL[way] #왼쪽으로 돌았
  tmpY,tmpX = y+dy[way],x+dx[way]
  if(inputL[tmpY][tmpX]!=0): #안가본데 아님
    noway+=1
    if(noway==4):#4번돌았
      tmpY,tmpX = y+dy[turnB[way]],x+dx[turnB[way]] #뒤돌아
      if(inputL[tmpY][tmpX]==1):#바다일때
        break
      else:
        y,x =tmpY,tmpX#이동
        noway=0
        continue#1단계로 돌아감
    else:#아직 4번 안돌
      continue#1단계로 돌아감
  else: #안가본데
    y,x =tmpY,tmpX
    inputL[y][x]=-1#갔음
    cnt+=1
    noway=0

print(cnt)
  
  