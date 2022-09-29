import sys
array=[]

n,m= map(int,sys.stdin.readline().split())
#1<=n,m<100

for _ in range(n):
    array.append(list(map(int,sys.stdin.readline().split())))

minL=[]
for eltN in range(n):#O(n)
    minL.append(min(array[eltN]))#O(m)

answer=max(minL)

print("{0}".format(answer))
