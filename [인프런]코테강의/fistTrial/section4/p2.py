'''
이분탐색-> 결정알고리즘에 사용

결정알고리즘
-> 답이 특정범위 안에 있음
-> 값의 범위 답이 될 수 있냐 없냐?
-> 값의 범위 반 날림
'''

'''
-> 값의 범위: 1~802
->(1+802)//2를 mid로 잡고 n를 구해봄
-> 답 아니라면(n개 보다 적게 나오면) 값 범위의 lt rt 줄여가며 계속 반복!
->만약 n개보다 많이 나오면 답 후보이므로 res에 저장해둠
->더 좋은 후보 생기면 계속 갱신해나감
'''

k,n = map(int,input().split())
inputList=list()

res=0
lt = 1
rt =-1
for i in range(k):
  tmp =int(input())
  inputList.append(tmp) #옆으로 들어오는게 아니라 줄바꿈 -> split() x 하나하나 받아야함
  if(rt<tmp):
    rt = tmp
    
def count(mid):
  num=0
  for i in list:
    num+=(i//mid)
  return num
  

while(lt<=rt):
  mid = (lt+rt)//2
  num = count(mid)
  
  if(num>=n):
    lt=mid+1
    # if(res<mid): 이렇게 안해줘도 lt가 더 좋은 값으로 움직이므로
    # 저절로 res는 더 좋은 값으로 갱신됌
    res = mid
  else:
    rt = mid-1

print(res)






