'''
몰겠...
'''
n,m = map(int,input().split())
inputList = list(map(int,input().split()))

lt = 0
rt = 1
tot=inputList[0]
cnt=0

while True:
  if(tot<m):
    if (rt<n):
      tot += inputList[rt]
      rt+=1
    else:
      break
  elif(tot==m):
    cnt+=1
    tot -= inputList[lt]
    lt+=1 #옆으로 밀고 가야하므로 lt를 변형!
  else:
    tot -= inputList[lt]
    lt+=1

print(cnt)
    
    
    