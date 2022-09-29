import sys

n,k = list(map(int,sys.stdin.readline().split()))

answer=0

while(n!=1):
    if(n%k==0):
        answer+=1
        n/=k
    else:
        answer+1
        n-=1

print(answer)

