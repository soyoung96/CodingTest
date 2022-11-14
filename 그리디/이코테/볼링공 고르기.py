import sys
n,m = map(int,sys.stdin.readline().split())

balls = list(map(int,sys.stdin.readline().split()))

answer = 0
for start in range(len(balls)-1):
    for end in range(start+1,len(balls)):
        m1 = balls[start]
        m2 = balls[end]
        if(m1 == m2):
            continue
        else:
            answer+=1 # 카운트 증가

print(answer)


