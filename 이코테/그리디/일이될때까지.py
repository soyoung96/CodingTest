n,k =map(int,input().split())
cnt=0

while (n!=1):
  while(n%k!=0):
    n-=1
    cnt+=1
    if(n==1):
      break
  if(n==1):
    break
  while(n%k==0):
    n = n//k
    cnt+=1
    if(n==1):
      break
  if(n==1):
      break

print(cnt)