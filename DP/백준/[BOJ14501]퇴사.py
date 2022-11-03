import sys

n = int(sys.stdin.readline())


inputL = []

dp=[0] *(n+1) #해당 인덱스 날짜에 끝날때 최대 페이가 저장됌

for _ in range(n):
    inputL.append(list(map(int,sys.stdin.readline().split())))



for startDay,tpL in enumerate(inputL,start=1):
    t = tpL[0]
    p = tpL[1]
    finalDay = startDay + t -1 #상담 끝 날짜
    if(finalDay <= n): #마지막 날짜를 넘기지 않으때만
        preMaxPay = max(dp[:startDay])
        dp[finalDay] =  max(preMaxPay+p,dp[finalDay]) #dp갱신


print(max(dp))

