'''
Devide and conquer->이분탐색 -> O(logN)
'''

n,m = map(int,input().split())

inputList = sorted(list(map(int,input().split())))

sp = 0
ep=n-1

while(sp<=ep):
  mid=(sp+ep)//2
  if(inputList[mid]==m):
    print(mid+1) # 인덱스 기준 ㄴㄴ 몇 번쨰 인지 ㅇㅇ
    break
  else:
    if(inputList[mid]>m):
      ep=mid-1
    else:
      sp=mid+1
  
      
  