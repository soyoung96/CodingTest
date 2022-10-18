import sys

n = int(sys.stdin.readline())

inputL = list(map(int,sys.stdin.readline().split()))

inputL.sort()

answer =0 #모험가 길드 답
count =0
for elt in inputL:
    count+=1
    if(count>=elt):# 팀결성
        answer+=1
        count=0

print(answer)

