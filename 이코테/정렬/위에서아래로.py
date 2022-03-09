n = int(input())
inputL=[]
for i in range(n):
  inputL.append(input())

def qsort(listIn):
  if(len(listIn)<=1):
    return listIn
  pivot =listIn[0]
  tail=listIn[1:]

  leftL = [ i for i in tail if i>pivot]
  rightL = [ i for i in tail if i<=pivot]

  return qsort(leftL)+ [pivot]+qsort(rightL)

inputL = qsort(inputL)

for j in inputL:
  print(j , end=" ")
