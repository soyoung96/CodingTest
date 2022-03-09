# l = int(input())
# inputList=list(map(int,input().split()))
# m = int(input())


# for i in range(m):
#   maxInd=inputList.index(max(inputList))
#   minInd=inputList.index(min(inputList))

#   inputList[maxInd]-=1
#   inputList[minInd]+=1

# print(max(inputList) - min(inputList))

l = int(input())
inputList=list(map(int,input().split()))
m = int(input())

cnt = [0] * 1001

for i in inputList:
  cnt[i] +=1
  
inputList.sort()
minVal = inputList[0]
maxVal = inputList[-1]

for i in range(m):
  if(cnt[maxVal] ==1):
    cnt[maxVal]-=1
    cnt[maxVal-1]+=1
    maxVal-=1
  elif(cnt[maxVal] >1):
    cnt[maxVal]-=1
    cnt[maxVal-1]+=1

  if(cnt[minVal] ==1):
    cnt[minVal]-=1
    cnt[minVal+1]+=1
    minVal+=1

  elif(cnt[minVal] >1):
    cnt[minVal]-=1
    cnt[minVal+1]+=1

print(maxVal-minVal)
  