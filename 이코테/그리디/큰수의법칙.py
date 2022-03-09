n,m,k =map(int,input().split())
inputL = list(map(int,input().split()))
inputL.sort(reverse = True)
cnt=0
result=0
first = inputL[0]
snd = inputL[1]
while(cnt<8):
  for j in range(k):
    result+=first
    cnt+=1
    if(cnt==m):
      break
  if(cnt==m):
    break
  else:
    result+=snd
    cnt+=1
      
print(result)
  