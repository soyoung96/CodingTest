'''
n명의 승객 타고 있음
구명보트 2명이하 + Mkg이하
승객 올 탈출 하려면 최소 필요한 구명보트개수 구하셈
'''

# n,m = map(int,input().split())
# inputList = list(map(int,input().split()))

# inputList.sort()

# cnt =0
# while(len(inputList)>0):
#   sumKG=0
#   cnt+=1
#   sumKG += inputList.pop(0)
#   if(len(inputList)==0):
#     break
#   else:
#     delList=[]
#     for i in range(len(inputList)-1,-1,-1):
#       if((sumKG+inputList[i])>m):
#         continue
#       else:
#         sumKG +=inputList[i]
#         delList.append(i)
#     for ind in delList:
#       inputList.pop(ind)
# print(cnt) # 3이상도 같은 배 탈수 있을떄


# n,m = map(int,input().split())
# inputList = list(map(int,input().split()))

# inputList.sort()

# cnt =0
# while(inputList): #inputList가 널이면 스톱
#   if(len(inputList)==1):
#     cnt+=1
#     break
#   if(inputList[0]+inputList[-1]>m):
#     inputList.pop()
#     cnt+=1
#   else:
#     inputList.pop()
#     inputList.pop(-1)
#     cnt+=1
    

# print(cnt) #문제처럼 2이상을 같은 배 탈 수 없다


'''
list.pop(0)의 문제점
맨앞 삭제시 모든 원소들을 앞으로 땡겨준다-> 비효율

but decueue로 하면 맨앞 가르키는 포인터만 증가
해주면 되므로 => 효율적
'''

#dequeue를 이용해보자
from collections import deque
n,m = map(int,input().split())
inputList = list(map(int,input().split()))

inputList.sort()
inputDeq = deque(inputList)

cnt =0
while(inputDeq): #inputList가 널이면 스톱
  if(len(inputDeq)==1):
    cnt+=1
    break
  if(inputDeq[0]+inputDeq[-1]>m):
    inputDeq.pop()
    cnt+=1
  else:
    inputDeq.pop()
    inputDeq.popleft()
    cnt+=1
    

print(cnt) #문제처럼 2이상을 같은 배 탈 수 없다


