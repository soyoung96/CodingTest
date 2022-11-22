# import sys
# from bisect import *
# from copy import deepcopy

# t = int(sys.stdin.readline())

# for _ in range(t):
#     n = int(sys.stdin.readline())
#     lastYNode = list(map(int,sys.stdin.readline().split()))
#     m = int(sys.stdin.readline())
#     chNodes=[]
#     for _ in range(m):
#         chNodes.append(list(map(int,sys.stdin.readline().split())))

#     impossible = False
#     lastYNode2 = deepcopy(lastYNode)
#     mustCH = []
#     for chNode in chNodes:
#         preE = chNode[0]
#         nextE = chNode[1]
#         preL = lastYNode[:lastYNode.index(preE)]
        
#         if(nextE not in preL): #잘못됌
#             impossible = True
#             break
#         else:
#             if((preE,nextE) in mustCH):
#                 del(mustCH[mustCH.index((preE,nextE))])
#             preL2 = lastYNode2[:lastYNode2.index(preE)]
#             if(nextE in preL2): #아직 교정 안된 거라면
            
#                 for nextPreE in lastYNode2[lastYNode2.index(nextE)+1:lastYNode2.index(preE)]: #역시 순위 바뀐 리스트 나중에 꼭 나와야 함
#                     mustCH.append((nextPreE,nextE))
#                 del(lastYNode2[lastYNode2.index(nextE)]) #앞 순위를 삭제하고
#                 lastYNode2.insert(lastYNode2.index(preE)+1,nextE) #뒷순위로 넣어줌
                

#     if(impossible):
#         print("IMPOSSIBLE")
#     elif(mustCH!=[]):
#         print("?")
#     else:
#         for elt in lastYNode2:
#             print(elt, end = " ")

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    indegrees = [0 for _ in range(n+1)]
    lastYNodes = list(map(int,sys.stdin.readline().split()))

    for ind in range(n-1): #자기보다 낮은 팀으로 가는 엣지 생성
        myTeam = lastYNodes[ind] #본인 팀
        lowerTeams = lastYNodes[ind+1:] #자기보다 낮은 팀
        graph[myTeam].extend(lowerTeams)
        for lowerTeam in lowerTeams:
            indegrees[lowerTeam]+=1 #차수 증가
        
    m = int(sys.stdin.readline())
    
    answer= [] #순위
    impossible = False
    cycle = False

    
    # print(graph)

    for _ in range(m): #기존 엣지 삭제하고 수정
        startT,endT = list(map(int,sys.stdin.readline().split()))
        if( startT not in graph[endT]):
            impossible = True
        else:
            del(graph[endT][graph[endT].index(startT)])#기존 엣지 삭제
            indegrees[startT]-=1 #차수 감소
            graph[startT].append(endT)#수정
            indegrees[endT]+=1 #차수 증가


    if(not impossible):
        q = deque([])
        for ind in range(1,n+1):
            indegree = indegrees[ind]
            if(indegree == 0):
                q.append(ind)
        
        
        while(q):
            if(len(q)>=2): #동일한 차수가 여러개->정확한 순위를 찾을 수 없음
                cycle = True
                break
            startT = q.popleft()
            answer.append(startT)
            
            for endT in graph[startT]:
                indegrees[endT] -=1
                if(indegrees[endT]==0):
                    q.append(endT)

    if(len(answer)==n):
        for team in answer:
            print(team,end = " ")
        print()
    elif(cycle):
        print("?")
    else:
        print("IMPOSSIBLE")





