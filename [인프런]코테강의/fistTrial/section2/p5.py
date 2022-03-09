# n,m = map(int,input().split())

# sumList=[]
# for i in range(n):
#   nNum = i+1
#   for j in range(m):
#     mNum =j+1
#     sumList.append(nNum + mNum)

# total=dict()
# for k in range(len(sumList)):
#   tempSum= sumList[k]
#   if(tempSum not in total.keys()):
#     total[tempSum] =1
#   else:
#     total[tempSum] +=1

# maxProperty =max(total.values())
# maxPropertyList=list()

# for i in total.keys():
#   if(total[i]==maxProperty):
#     maxPropertyList.append(i)

# maxPropertyList.sort()

# for i in maxPropertyList:
#   print(i,end=" ")

n,m = map(int,input().split())

cnt = [0]*(n+m+1)

for i in range(1,n+1):
  for j in range(1,m+1):
    cnt[i+j]+=1
max=-1
for i in range(1,n+m+1):
  if(max<cnt[i]):
    max = cnt[i]

for i in range(len(cnt)):
  if(cnt[i]==max):
    print(i,end=" ")


