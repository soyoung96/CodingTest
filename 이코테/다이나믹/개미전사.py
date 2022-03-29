n =int(input())
inputL = list(map(int,input().split()))
inputL = [0]+inputL
maxL=[0]*(n+1)

for i in range(1,n+1):
  if(i == 1):
    maxL[i] = inputL[i]
    
  elif(i == 2):
    maxL[i] = max(inputL[i],inputL[i-1])
    
  else:
    maxL[i] = max(maxL[i-2]+inputL[i],maxL[i-1])

print(maxL[n])