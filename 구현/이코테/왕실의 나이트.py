import sys

mapL = [[0]*(8+1) for _ in range(8+1)]

start = sys.stdin.readline().rstrip()

dx = [2,2,1,-1,-2,-2,1,-1]
dy = [1,-1,2,2,1,-1,-2,-2]

y = ord(start[0])-ord("a")+1
x = int(start[1])

def chkY(y):
    if(1<=y<=8):
        return True #그쪽으로 갈 수 있다
    else:
        return False


def chkX(x):
    if(1<=x<=8):
        return True #그쪽으로 갈 수 있다
    else:
        return False

answer = 0

for i in range(8):
    nextY = y +dy[i]
    nextX = x + dx[i]
    if(chkY(nextY) and chkX(nextX)):
        answer+=1

print(answer)






