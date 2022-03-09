def reverse(x):
  res=0
  while x>0:
    t = x%10
    res = res*10 + t
    x = x//10
  return res

# def isPrime(x):
#   cnt=0
#   if(x==1):
#     return False
#   else:
#     for i in range(2,x+1):
#       if(x%i ==0):
#         cnt+=1
#     if(cnt==1):
#       return True
#     else:
#       return False

def isPrime(x):
  if(x==1):
    return False
  else:
    for i in range(2,x//2+1): #for else-> for에서 break발생 x면!
                              #x가 2일때 range(2,2)->아예 for문 동작 x
      if(x%i ==0):
        return False
    else:
      return True

n =int(input())
nList = list(map(int,input().split()))

for k in range(n):
  tmp=reverse(nList[k])
  if(isPrime(tmp)):
    print(tmp,end=" ")




  
  
  


    
  