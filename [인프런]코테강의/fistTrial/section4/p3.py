'''
n개 곡, 곡 순서 유지,
m개의 DVD에 녹음 하나의 dvd당 가장 작은 용량으로->
                          check(x)랑 비교(y축)
용량 크기=>0~ sum(List) => 구해야하는 값 (x축) -> 최대한 작게
'''
n,m = map(int,input().split())
inputList=list(map(int,input().split()))

lt =0
rt=sum(inputList)

def check(mid): #x를 집어 넣을 때 y가 나오게끔
  dvdCnt=1
  tmpSum =0
  for j in inputList:
    tmpSum+=j
    if(tmpSum>mid):
      tmpSum=j
      dvdCnt+=1

  return dvdCnt

maxx = max(inputList)    
  
res=0
while(lt<=rt):
  mid = (lt+rt)//2

  if(mid>=maxx and check(mid)<=m):
    rt = mid-1 
    res=mid
  else:
    lt = mid+1

print(res)
