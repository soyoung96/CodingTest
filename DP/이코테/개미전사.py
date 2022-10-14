import sys

n = int(sys.stdin.readline())

inputL = [0]

inputL.extend(list(map(int,sys.stdin.readline().split())))

dp=[-1] * (n+1)

#탑다운
def findMaxFood(inputLLenth):
    global dp
    global inputL
    if(dp[inputLLenth] == -1): #계산 아직 안했으면

        if(inputLLenth==1):
            dp[1] = inputL[1]
            return dp[1]

        if(inputLLenth==2):
            if(findMaxFood(inputLLenth-1)>inputL[inputLLenth]):
                dp[2] = findMaxFood(inputLLenth-1)
            else:
                dp[2] = inputL[inputLLenth]
            return dp[2]

        
        opt1 = findMaxFood(inputLLenth-2)+inputL[inputLLenth]
        opt2 = findMaxFood(inputLLenth-1)
        if(opt1> opt2):
            dp[inputLLenth] = opt1 #가장 많은 푸드 등록
            
        else:
            dp[inputLLenth] = opt2 #가장 많은 푸드 등록
        return dp[inputLLenth]

    else:#계산 한 적 있으면
        return dp[inputLLenth]


print(findMaxFood(n))


