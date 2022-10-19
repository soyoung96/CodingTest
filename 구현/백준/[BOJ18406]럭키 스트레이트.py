import sys

n = sys.stdin.readline().rstrip()

lenN = len(n)

leftSum =0
rightSum =0
for i in range(lenN):
    if(i >= (lenN/2)): #오른쪽 자리수
        rightSum+=int(n[i])
    else:
        leftSum+=int(n[i])

if(leftSum ==rightSum):
    print("LUCKY")
else:
    print("READY")
