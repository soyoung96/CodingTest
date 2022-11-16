import sys
from itertools import permutations

n = int(sys.stdin.readline())

numL = list(map(int,sys.stdin.readline().split()))

expL = list(map(int,sys.stdin.readline().split()))

realexpL = []

for ind,elt in enumerate(expL):
    realexpL.extend([ind]*elt )


maxSum = int(-1e11)
minSum = int(1e11)
for expL in permutations(realexpL,len(realexpL)):
    sum =numL[0]
    for numInd,exp in enumerate(expL): 
        a2 = numL[numInd+1]    
        if(exp==0):#+
            sum+=a2
        elif(exp==1):#-
            sum-=a2
        elif(exp==2):#*
            sum*=a2
        else:
            if(sum<0):#음수면
                sum = -(-(sum)//a2)
            else:
                sum = sum//a2
    if(sum>maxSum):
        maxSum = sum
    if(sum<minSum):
        minSum = sum


print(maxSum)
print(minSum)

# import sys
# from itertools import permutations

# n = int(sys.stdin.readline())

# numL = list(map(int,sys.stdin.readline().split()))

# add,minus,cross,recross = map(int,sys.stdin.readline().split())

# maxSum = int(-1e11)
# minSum = int(1e11)

# def dfs(i,now):
#     global add,minus,cross,recross,maxSum,minSum
#     if(i == n):
#         if(now<minSum):
#             minSum = now
#         if(now>maxSum):
#             maxSum = now
#         return now
    
#     if(add!=0):
#         add-=1
#         dfs(i+1,now+numL[i])
#         add+=1
#     if(minus!=0):
#         minus-=1
#         dfs(i+1,now-numL[i])
#         minus+=1
#     if(cross!=0):
#         cross-=1
#         dfs(i+1,now*numL[i])
#         cross+=1
#     if(recross!=0):
#         recross-=1
#         if(now<0):
#             dfs(i+1,-((-now)//numL[i]))
#         else:
#             dfs(i+1,now//numL[i])      
#         recross+=1


# dfs(1,numL[0])
# print(maxSum)
# print(minSum)


