import sys

n = int(sys.stdin.readline())

moneys = list(map(int,sys.stdin.readline().split()))

moneys.sort() #O(1000)

target = 1

for money in moneys:
    if(money<=target):#target 만들 수 있음
        target+=money
    else:
        break

print(target)




