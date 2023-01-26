import sys


n,k = map(int,sys.stdin.readline().split())

dp = [0 for _  in range(k+1)]

moneys = []

for _ in range(n):
    money = int(sys.stdin.readline())
    if(money<=k):
        moneys.append(money)


for money in moneys: #O(100 *10000)
    dp[money]+=1 #경우의 수 증가
    for nextMoney in range(money+1,k+1):
        dp[nextMoney] += dp[nextMoney-money]

print(dp[k])


