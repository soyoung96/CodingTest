import sys

while(True):
    n = int(sys.stdin.readline())
    if(n == 0):
        break
    dp  = [[0] * (n+1) for _ in range(n+1)] #(w개수,h개수) 2차원 배열

    for h in range(1,n+1):
        dp[0][h] = 1 #다 h밖에 없으면 문자열 경우의 수 1
    
    
    for w in range(1,n+1):
        for h in range(n):
            if(h==0): #h가 0없으면
                dp[w][h] = dp[w-1][h+1]
            else: #h가 하나라도 있으면
                dp[w][h] = dp[w-1][h+1] + dp[w][h-1]
    
    print(dp[n][0])

    

