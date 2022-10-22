import sys

s = list(sys.stdin.readline().rstrip())

answer =[]

sum=0
for elt in s:
    if(elt.isdigit()):
        sum += int(elt)
    else:
        answer.append(elt)

answer.sort()

answer.append(sum)

for elt in answer:
    print(elt,end="")
