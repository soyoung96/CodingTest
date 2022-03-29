n,m = map(int,input().split())
inputList = list(map(int,input().split()))

def getDD(inputL,h):
  sum =0
  for i in inputL:
    tmp = i - h
    if(tmp>=0):
      sum+=tmp
  return sum
lt,rt = 0,1000000000

while(lt<=rt):
  mid = (rt + lt)//2
  DD =getDD(inputList,mid)
  if(DD<m):
    rt = mid-1
  else:
    result = mid
    lt= mid+1

print(result)
  