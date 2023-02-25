import sys

lp = 1

n,k,d = map(int,sys.stdin.readline().split())

rp = n


rightL = []

for _ in range(k):
    a,b,c = map(int,sys.stdin.readline().split())
    rightL.append((a,b,c))

def cntBox(mid,rightL): #mid 이하로 들어가는 도토리 개수
    sum =0
    
    for a,b,c in rightL:
        if(a<=mid):
            #print(a,mid,b)
            sum+=1
            realB = min(b,mid)
            sum += ((realB - a)//c)

    return sum

minMid =int(1e7)
while(lp<=rp):
    mid = (lp+rp)//2
    # print(mid)
    rtV = cntBox(mid,rightL)
    # print(rtV)
    if(rtV<d): # 상자 번호 내림
        lp = mid +1
    else:
        if(minMid > mid):
            minMid = mid
        rp = mid - 1

print(minMid)




