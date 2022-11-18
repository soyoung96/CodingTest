import sys
maxNum = -1 #가장큰 어글리값

n = int(sys.stdin.readline())
uglyNums = [2,3,5]
notUglyNums = [] #어글리수 아닌 수
total = 0
while(total<n):
    if(total==0):#못생수
        maxNum = 1
        total +=1
    
    else:
        maxNum+=1
        goContinue = False
        for uglyNum in uglyNums:
            fistForBreak = False
            if(maxNum%uglyNum==0):
                for notUglyNum in notUglyNums:
                    if(maxNum%notUglyNum==0): #not ugly 수
                        notUglyNums.append(maxNum)
                        fistForBreak = True
                        break
                if(fistForBreak):
                    goContinue = True
                    break

                #여기까지 오면 못생긴수
                total +=1
                goContinue = True
                break
        if(goContinue):
            continue
        #어글리 수 아님
        notUglyNums.append(maxNum)
        continue

print(maxNum)
                

