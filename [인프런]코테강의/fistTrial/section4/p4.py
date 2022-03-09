'''
c 마리의 말
1-n좌표의 마굿간
y-> 선택되는 마굿간이 말c 보다 작으면 안됑 (제한조건)
결정하고자 하는 것x-> 가장 가까운 두말의 거리 -> 최대가 되게끔

제한조건(y)하에 내가 원하는 x를 결정해라 -> 결정 알고리즘
'''

n,c = map(int,input().split())

inputList=list()
for i in range(n):
  inputList.append(int(input()))
inputList.sort()

lt=0
rt = inputList[-1] -inputList[0]

def check(mid):
  numPlace=1
  lenth=0
  for i in range(n-1):
    lenth+= inputList[i+1]-inputList[i]
    if(lenth>=mid):
      numPlace+=1
      lenth=0
    
  return numPlace

res=0
while(lt<=rt):
  mid = (lt+rt)//2
  if(check(mid)>=c):
    lt= mid+1
    res=mid
  else:
    rt=mid-1

print(res)
    