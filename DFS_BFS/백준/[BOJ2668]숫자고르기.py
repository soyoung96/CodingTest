import sys
sys.setrecursionlimit(int(1e7))

def dfs(startInd,ind,chart,dfsIterNum,visited): #O(100)
    visited[ind] = True #방문    
    if(chart[ind] == startInd):
        ans[0] = dfsIterNum
    else:
        if(visited[chart[ind]] != True): #방문한 적 없으면
            dfs(startInd,chart[ind],chart,dfsIterNum+1,visited)
        else:
            ans[0] = -1 #같은 집합 불가


n = int(sys.stdin.readline())

chart = [-1]

for _ in range(n):
    chart.append(int(sys.stdin.readline()))

maxAns =0
ans = [0]

maxVisited = []
for startInd in range(1,n+1): #O(100*300)
    if(startInd not in maxVisited): #이미 집합 포함된 곳은 방문 X    
        visited = [False] *(n+1) #O(100)
        dfs(startInd,startInd,chart,1,visited)#O(100)
        if(ans[0]>0): #같은 집합 결과 나옴
            maxAns += ans[0] # maxAns갱신
            for ind in range(1,n+1):#O(100)
                if(visited[ind] == True):
                    maxVisited.append(ind)

print(maxAns)
maxVisited.sort()#O(100log100)
for elt in maxVisited:
    print(elt)







