# totalList=[0]*(20+1)
# for i in range(len(totalList)):
#   totalList[i]=i
  
# for i in range(10):
#   sInd,eInd = map(int,input().split())
#   totalList[sInd:eInd+1]=list(reversed(totalList[sInd:eInd+1]))

# for i in range(1,len(totalList)):
#   print(totalList[i],end=" ")
totalList=list(range(0,21))
  
for i in range(10):
  sInd,eInd = map(int,input().split())
  for j in range((eInd-sInd+1)//2):
    totalList[sInd+j],totalList[eInd-j] = totalList[eInd-j],totalList[sInd+j]

for i in range(1,len(totalList)):
  print(totalList[i],end=" ")
