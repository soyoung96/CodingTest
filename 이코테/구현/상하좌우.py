n = int(input())
#R U L D
dx = [1,0,-1,0]
dy=[0,-1,0,1]
inputL = list(input().split())
way4 = {"R":0,"U":1,"L":2,"D":3}
position =[1,1] #y,x
for i in inputL:
  tmpX=position[1]+dx[way4[i]]
  tmpY=position[0]+dy[way4[i]]
  if((tmpX>n or tmpX<1) or (tmpY>n or tmpY<1)):
    continue
  else:
    position[1]=tmpX
    position[0]=tmpY
  
for i in position:
  print(i,end =" ")
 