# x = int(input())
# def what(x):
#   if(x%5 == 0):
#     return x//5
#   elif(x%3 ==0):
#     return x//3
#   elif(x%2 ==0):
#     return x//2
#   else:
#     return x-1
# cnt=0
# while(x!=1):
#   x =what(x)
#   cnt+=1
# print(cnt) ====> 그리디! ==> 위의 문제에서는 그리디 사용해서 최적해가 도출된다는 근거가 없다 => 완탐 ㄱㄱ => 그럼 다이나믹?

x = int(input())
dpL=[0] * 30001

for i in range(2,x+1):
  
  dpL[i] = dpL[i-1] +1
  if(i % 5==0):
    dpL[i] = min(dpL[i],dpL[i//5] +1)
  if(i % 3==0):
    dpL[i] = min(dpL[i],dpL[i//3] +1)
  if(i % 2==0):
    dpL[i] = min(dpL[i],dpL[i//2] +1)

print(dpL[x])
    
  
  
  

  



  