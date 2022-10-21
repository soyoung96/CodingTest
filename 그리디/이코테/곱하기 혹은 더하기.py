import sys

s = sys.stdin.readline().rstrip()

sum = int(s[0])
for ind in range(1,len(s)):
    tmp = s[ind]
    if(1<=int(sum) and 1<=int(tmp)): #x가 나음
        sum = int(sum) * int(tmp)
    else:
        sum = int(sum) + int(tmp)

print(sum)

