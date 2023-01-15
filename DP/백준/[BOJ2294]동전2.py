import sys

n,k = map(int,sys.stdin.readline().split())
INF = int(1e10)
moneyL = []
dp = [INF for _ in range(k+1)]

for _ in range(n): #100
    money = int(sys.stdin.readline())
    if(money<=k): #money>k이면 k 만드는데 안쓰임
        moneyL.append(money)
        dp[money] = 1

for ind in range(k+1): #1000000000
    minTry = dp[ind] #사용한 동전의 최소 개수
    for money in moneyL: #사용한 동전의 최소 개수 갱신
        preMoney = ind - money
        if(preMoney>0):
            newTry = dp[preMoney]+1
            if(minTry>newTry):
                minTry = newTry
    dp[ind] = minTry

if(dp[k] == INF):
    dp[k] = -1
print(dp[k])

    






