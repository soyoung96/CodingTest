# n = int(input())
# inputList=list(map(int,input().split()))

# restore=[0] * n
# index=int()
# cnt=[0]*n

# for i in range(1,n+1):
#   go=inputList[i-1]
#   moreGo=sum(cnt[:go])
#   finalGo = go+moreGo
#   if(cnt[finalGo]==0):
#     cnt[finalGo]+=1
#     restore[finalGo] = i
#   else:
#     while(cnt[finalGo]==1):
#       finalGo+=1
#     cnt[finalGo]+=1
#     restore[finalGo] = i

# for i in restore:
#   print(i,end=" ")

n = int(input())
inputList=list(map(int,input().split()))
restore=[0] * n

for i in range(n):
  for j in range(n):
    if(inputList[i]==0 and restore[j]==0):#얼만큼 더 가야하는지 , j는 거기 넣어도 되는지
      restore[j]=i+1
      break

    elif(restore[j]==0):
      inputList[i]-=1

for i in restore:
  print(i,end=" ")   

  