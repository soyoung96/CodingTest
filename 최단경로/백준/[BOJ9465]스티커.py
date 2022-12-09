import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline()) 
    dpL = []
    dpL.append(list(map(int,sys.stdin.readline().split())))
    dpL.append(list(map(int,sys.stdin.readline().split())))

    maxNm2 = -1
    for ind in range(n):
        if(ind==0):
            continue
        elif(ind == 1):
            dpL[0][ind] = dpL[1][ind-1] + dpL[0][ind]
            dpL[1][ind] = dpL[0][ind-1] + dpL[1][ind]
            maxNm2 = max(maxNm2,dpL[0][ind-1],dpL[1][ind-1])
        else:
            dpL[0][ind] = max(dpL[1][ind-1] + dpL[0][ind],maxNm2+dpL[0][ind])
            dpL[1][ind] = max(dpL[0][ind-1] + dpL[1][ind],maxNm2+dpL[1][ind])
            maxNm2 = max(maxNm2,dpL[0][ind-1],dpL[1][ind-1])
    
    answer = max(maxNm2,dpL[0][n-1],dpL[1][n-1])

    print(answer)




        
    