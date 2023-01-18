import sys
from collections import deque
'''
위상정렬 사용 이유
-> 모든 건물을 짓는 것이 가능한 입력만 주어진다.
'''
n = int(sys.stdin.readline())

anstimes = [0 for _ in range(n+1)]
times = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]

for buildingNum in range(1,n+1):#O(500 * 500)
    inputL = list(map(int,sys.stdin.readline().split()))
    for ind,elt in enumerate(inputL):
        if(elt == -1):
            break
        if(ind == 0): #소요시간
            times[buildingNum] = elt
        else: #먼저 지어져야하는 건물
            graph[elt].append(buildingNum)
            inDegree[buildingNum]+=1

queue = deque([])

for buildingNum in range(1,n+1):
    if(inDegree[buildingNum]==0):
        queue.append((buildingNum,times[buildingNum])) #인 차수0이면 queue삽입

while(queue):
    completeBuildingNum,completeT = queue.popleft() #다 지어진 건물,지어진 시간
    anstimes[completeBuildingNum] = completeT
    for nextBuilding in graph[completeBuildingNum]:
        inDegree[nextBuilding]-=1
        nextCompleteT = completeT + times[nextBuilding]
        anstimes[nextBuilding] = max(anstimes[nextBuilding],nextCompleteT)
        if(inDegree[nextBuilding]==0):     
            queue.append((nextBuilding,anstimes[nextBuilding]))

for buildingNum in range(1,n+1):
    print(anstimes[buildingNum])
        





