# import sys

# n = int(sys.stdin.readline())

# manL = []

# manL.extend(list(map(int,sys.stdin.readline().rstrip().split())))

# dp = [[1,i] for i in manL]


# for ind,man in enumerate(manL):
#     maxLength = -1 #man 보다 큰 man들이 마지막에 올때 가장 큰 길이
#     for pre in range(0,ind):
#         preLength,preMan = dp[pre]#해당 man 이 맨 끝에 왔을때 길이,man 이전에 오는 man
#         if(preMan>man): #전투력이 더 높은 man이 앞에올때            
#             if(maxLength<preLength):
#                 maxLength = preLength
   
#     dp[ind][0] = max(dp[ind][0],maxLength+1)


# print(n -max(dp)[0])

import sys

n = int(sys.stdin.readline())

manL = []

manL.extend(list(map(int,sys.stdin.readline().rstrip().split())))

dp = [1 for _ in manL]


for i in range(1,n):
    for j in range(i):
        if(manL[j]>manL[i]):
            dp[i] = max(dp[j]+1,dp[i])



print(n -max(dp))
