n,m = map(int,input().split())
inputL=[]
for i in range(n):
  inputL.append(int(input()))

inputL.sort()
inputL = [0]+inputL
minL =[-1] * 10001
for i in range(1,len(inputL)):
  minL[inputL[i]] = 1

for i in range(1,m+1):
  for j in range(1,len(inputL)):
    if((i-inputL[j])>=0):
      if(minL[i-inputL[j]] != -1):
        minL[i] = min(minL[i-inputL[j]] +1,minL[i])

print(minL[m])
  
    
    