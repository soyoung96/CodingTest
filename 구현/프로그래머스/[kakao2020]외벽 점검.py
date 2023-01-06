from itertools import permutations

def delWeakE(weakcopy,distE,startWeakE,n): #15 #커버한 weak 삭제
    endDist = startWeakE+distE
    if(n<=endDist): #n-1에서 0 이후로 넘어감
        for weakE in weakcopy:
            weakcopy.pop(weakcopy.index(weakE))
        
            
    else: #n-1에서 0 이후로 넘어가지 않음
        delWeakList = []
        for weakE in weakcopy: #for문에 사용되는 리스트는 pop이나 append 같은거로 변경하는 거 아님!!! -> 오류조심!
            if(startWeakE<= weakE <= endDist):
                delWeakList.append(weakE)
        for delWeakE in delWeakList: 
            weakcopy.pop(weakcopy.index(delWeakE))
        
def solution(n, weak, dist):
    minFriendNum = 100
    for orderedDist in permutations(dist,len(dist)): # 8P8
        for startWeakInd in range(len(weak)):
            startWeak = weak[startWeakInd]
            weakcopy = []
            for weakE in weak:
                newWeakE = weakE-startWeak
                if(newWeakE<0): #음수면 왼쪽 방향으로 0을 가로지름
                    newWeakE = n + newWeakE
                weakcopy.append(newWeakE)
            weakcopy.sort()
            
            friendNum = 0 #필요한 친구수
            for orderedDistE in orderedDist:
                friendNum+=1 #필요한 친구수 증가
                # if(orderedDist == (4,2,3,1)):
                #     print(friendNum)
                #     print(orderedDistE)
                #     print(weakcopy[0])
                #     print(weakcopy)
                delWeakE(weakcopy,orderedDistE,weakcopy[0],n) #15 #커버한 weak 삭제
                if(weakcopy == []): #모든 weak 다 커버함
                    break
            if(weakcopy == []): #모든 weak 다 커버함
                
                if(minFriendNum>friendNum):
                    # print(friendNum)
                    # print(orderedDist)
                    minFriendNum = friendNum #minFriendNum갱신
    
    if(minFriendNum == 100): #취약지점 전부 전검 할 수 없음
        minFriendNum = -1
    
    return minFriendNum