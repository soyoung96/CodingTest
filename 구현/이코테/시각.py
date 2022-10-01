import sys

n = int(sys.stdin.readline())

answer =0

for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            if((str(3) in str(s)) or (str(3) in str(m)) or (str(3) in str(h))):
                answer+=15
                

print(answer)



