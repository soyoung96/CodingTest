n = int(input())
scoreList=list(map(int,input().split()))
scoreSum =0

for i in range(n):
  scoreSum+=scoreList[i]

meanScore = int(round(scoreSum/len(scoreList),0))

minSubScore = 10000
minSubScoreInd =-1
for i in range(n):
  subScore = abs(scoreList[i]-meanScore)
  if(subScore<minSubScore):
    minSubScore = subScore
    minSubScoreInd = i
  elif(subScore==minSubScore):
    if(scoreList[minSubScoreInd]<scoreList[i]):
      minSubScore = subScore
      minSubScoreInd = i
        
    
print("{0:d} {1}".format(meanScore,minSubScoreInd+1))




