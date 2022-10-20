import sys
from bisect import bisect_left,bisect_right

n,x = map(int,sys.stdin.readline().split())

inputL = list(map(int,sys.stdin.readline().split()))

inputL.sort() #오름차순 정렬

answer = bisect_right(inputL,x) - bisect_left(inputL,x)

if(answer == 0):
    print(-1)
else:
    print(answer)
