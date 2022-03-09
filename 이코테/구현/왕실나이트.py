# n = input()
# x=ord(n[0])-ord("a")+1
# y = int(n[1])
# #R U L D
# dx = (1,0,-1,0)
# dy = (0,-1,0,1)
# way4 = [[2*dy[i]+dy[j],2*dx[i]+dx[j]] for i in [0,2] for j in [1,3]]
# way4_ = [[2*dy[i]+dy[j],2*dx[i]+dx[j]] for i in [1,3] for j in [0,2]]
# way8 = way4+way4_

# position = [y,x]

# cnt=0
# for i in way8:
#   tmpY = position[0]+ i[0]
#   tmpX = position[1]+ i[1]
#   if((tmpY<1 or tmpY>8)or(tmpX<1 or tmpX>8)):
#     continue
#   else:
#     cnt+=1
  
# print(cnt)

n = input()
x=ord(n[0])-ord("a")+1
y = int(n[1])
#R U L D
dx = (1,0,-1,0)
dy = (0,-1,0,1)
way8 = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]] #이정도는 그냥 경우의수 생각이 편함

position = [y,x]

cnt=0
for i in way8:
  tmpY = position[0]+ i[0]
  tmpX = position[1]+ i[1]
  if((tmpY<1 or tmpY>8)or(tmpX<1 or tmpX>8)):
    continue
  else:
    cnt+=1
  
print(cnt)