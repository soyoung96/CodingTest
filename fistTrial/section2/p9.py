# n = int(input())
# getList=list()
# for i in range(n):
#   tmpList = list(map(int,input().split()))
#   getList.append(tmpList)

# def getMoney(x):
#   gameList=[0] * 7
#   for i in x:
#     gameList[i]+=1

#   max=-1
#   maxInd=-1
#   for i in range(7):
#     if(gameList[i]>=max):
#       max=gameList[i]
#       maxInd=i

#   if(max==3):
#     return 10000+maxInd*1000
#   elif(max==2):
#     return 1000+maxInd*100
#   else:
#     return i *100
    
# moneyList=list()
# for i in range(n):
#   money = getMoney(getList[i])
#   moneyList.append(money)

# print(sorted(moneyList)[-1])


n = int(input())
maxMoney=-1
for i in range(n):
  tmp=0
  a,b,c = sorted(list(map(int,input().split())))

  if (a==b) and(b==c): # 경우를 가장 엄격한거부터 적어야함
    tmp= 10000+a*1000
  elif(a==b or a==c):
    tmp = 1000+a*100
  elif (b ==c):
    tmp = 1000+b*100
  else:
    tmp = c* 100

  if(tmp>maxMoney):
    maxMoney = tmp

print(maxMoney)

  
  
  


