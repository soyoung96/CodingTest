import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

def check(n,val): #n*n행렬에서 val보다 작은 수 가 몇개인지 리턴 #O(1e5)
    ans = 0
    for x in range(1,n+1):
        ans+=min(n,val//x)

    return ans

start = 0
end = k #O(1e10)

mid =-1
ansMid = 0
while(start<=end):
    mid = (start+end)//2
    ans = check(n,mid)
    if(k<=ans): #mid가 B[k]보다 같거나 크다
        ansMid = mid
        end=mid-1
    else: #mid가 B[k]보다 작다
        start = mid+1

print(ansMid)