n = int(input())
inputN = list(map(int,input().split()))
m = int(input())
inputM = list(map(int,input().split()))

inputN.sort()

def findBS(inL,elt):
  rt,lt = len(inL)+1,1
  inL = [0]+inL
  while(lt<=rt):
    mid = (rt+lt)//2
    if(inL[mid]==elt):
      return True
    elif(elt<inL[mid]):
      rt=mid-1
    else:
      lt =mid+1
  return False

for elt in inputM:
  if(findBS(inputN,elt)):
    print("yes",end=" ")
  else:
    print("no",end=" ")
  
        
      
  