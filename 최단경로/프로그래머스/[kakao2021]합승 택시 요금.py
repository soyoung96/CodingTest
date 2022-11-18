from pprint import pprint
from collections import deque
def solution(n, s, a, b, fares):
    
    INF = int(1e11)
    graph = [[INF]*(n+1) for _ in range(n+1)]
    # path = [[-1]*(n+1) for _ in range(n+1)]
    # answer = 0
    for fare in fares:
        c,d,f = fare[0],fare[1],fare[2]
        graph[c][d] = f
        graph[d][c] = f
        # path[c][d] = c
        # path[d][c] = d
        
    for i in range(1,n+1):
        graph[i][i] = 0
        # path[i][i] = i
        
    for mid in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                # graph[start][end] = min(graph[start][end],graph[start][mid]+graph[mid][end])
                
                if(graph[start][end]>graph[start][mid]+graph[mid][end]):
                    graph[start][end] = graph[start][mid]+graph[mid][end]
#                     path[start][end] = path[mid][end]
    
#     rootAB = deque([])
    
#     start = a
#     end = b
#     rootAB.appendleft(end)
#     while(path[start][end] != start): #-> 이러면 갱신되었던거
#         rootAB.appendleft(path[start][end])
#         end = path[start][end] #끝 점 직전 
#     rootAB.appendleft(start)
    
#     minSMid = int(1e11)
#     for node in rootAB:
#         if(minSMid>graph[s][node]):
#             minSMid= graph[s][node]
            
#     answer = minSMid + graph[a][b]

    answer = int(1e11)
    for mid in range(1,n+1):
        total = graph[s][mid]+graph[mid][a]+graph[mid][b]
        if(answer>total):
            answer = total
                         
    
    return answer