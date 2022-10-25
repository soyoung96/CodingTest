import sys

n= int(sys.stdin.readline())

inputL = list(map(int,sys.stdin.readline().split()))

start = 0
end = n-1

answer = False
while start<=end:
    mid = (start + end)//2
    val = inputL[mid]
    if(val==mid):
        print(val) #정답 출력
        answer = True
        break
    elif(val<mid): #오른쪽 봐야함
        start = mid+1
    else: #왼쪽 봐야함
        end = mid-1

if(not answer):#고정점 없음
    print(-1) 

