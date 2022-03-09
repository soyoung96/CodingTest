# n = int(input())

# primeCnt=0

# for i in range(2,n+1):
#   cnt =0
#   for j in range(1,i):
#     if(i%j ==0):
#       cnt+=1
#   if(cnt==1): # cnt이 단 1개여야->소수
#     primeCnt+=1
  
      
# print(primeCnt)

# 소수구하는데 가장 빠른 것-> 에라토스테네스체

n = int(input())

primeCnt=0
primeChkList=[0]*(n+1)

for i in range(2,n+1):
  if(primeChkList[i]==0):
    primeCnt+=1
    for j in range(i,n+1,i):
      primeChkList[j]+=1

    
  
      
print(primeCnt)