import sys

n = int(sys.stdin.readline())

inputL = sorted(list(map(int,sys.stdin.readline().split()))) # 100000log100000
# -99 -2 -1 4 98

lp = 0
rp = len(inputL)-1

minAbsMw = int(1e10)
ansLp = -1
ansRp = -1
while(lp<rp):
    lw = inputL[lp]
    rw = inputL[rp]
    mw = lw+rw
    absMw = abs(mw)
    if(absMw<minAbsMw):
        minAbsMw = absMw #갱신
        ansLp = lp
        ansRp = rp
    if(mw<0): # lp를 앞으로 옮긴다
        lp+=1
    else:
        rp-=1

print(inputL[ansLp],inputL[ansRp])






   


