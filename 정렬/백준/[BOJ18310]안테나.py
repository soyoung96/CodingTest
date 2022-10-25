import sys

n = int(sys.stdin.readline())

inputArr = list(map(int,sys.stdin.readline().split()))

inputArr.sort() #O(n)

print(inputArr[(n-1)//2])


