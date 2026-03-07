import sys
from collections import deque

n,k = map(int,sys.stdin.readline().rstrip().split())
a = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
b = sorted(list(map(int,sys.stdin.readline().rstrip().split())),reverse = True)
changeCtn = 0
for i in range(len(a)):
    if(a[i]<b[i] and changeCtn<k):
        a[i],b[i] = b[i],a[i]
        changeCtn+=1
    else:
        break

print(sum(a))