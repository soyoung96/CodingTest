import sys

n = int(sys.stdin.readline()) #<=50

creinL =list(map(int,sys.stdin.readline().split())) 

m = int(sys.stdin.readline())#<=10000

boxL =list(map(int,sys.stdin.readline().split()))

boxL.sort(reverse=True)
creinL.sort(reverse=True)

completeBoxNum = 0

completeBoxs = [False for _ in range(m)]

ans=0
while(completeBoxNum<m): #O(200*10000)
    
    useCreinNum = 0
    notExistAns = False
    for ind,box in enumerate(boxL):
        
        if(not completeBoxs[ind]):#아직 옮기지 않은 박스
            crein = creinL[useCreinNum]# 해당 크레인 들 수 있는 무게
            if(useCreinNum==0 and crein<box): #가장 성능좋은 크레인으로도 못 옮김
                ans = -1
                notExistAns = True
                break
            else:
                if(crein>=box): #해당 박스 옮기기 가능
                    useCreinNum+=1
                    completeBoxs[ind] = True
                    completeBoxNum+=1
        if(useCreinNum== n or ind ==m-1): #크레인 다 쓰거나 박스가 마지막 까지 내려왔을 때
            ans+=1
            # print(completeBoxNum)
            # print(completeBoxs)
            break
    
                
                
    if(notExistAns):
        break



print(ans)




                





