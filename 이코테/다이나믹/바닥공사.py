n = int(input())

maxL= [0] * 1001
for i in range(1,n+1):
  if(i==1):
    maxL[i] = 1
  elif(i==2):
    maxL[i] = 3
  else:
    maxL[i]= maxL[i-1]+maxL[i-2]*2

print(maxL[n])