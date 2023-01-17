import sys
from collections import deque

'''
위상정렬대신 플로이드워셜 쓴 이유
1. 위상정렬의 경우 전체 그래프에서의 순서를 따진다!
-해당 문제의 경우 그래프가 하나의 그래프가 아니라 2개 3개 일 수 있다. -> 순서 알 수 없는 경우
-> 과정이 복잡하다

- 매 50000번 마다 위상정렬 해놓은 리스트에서 순서를 찾아야함
-> 시간 복잡도가 매우 커짐

'''
n,k = map(int,sys.stdin.readline().split())
INF = int(1e11)

graph = [[INF] *(n+1) for _ in range(n+1)]#O(400)

for selfNode in range(1,n+1):#O(400)
    graph[selfNode][selfNode] = 0
    
for _ in range(k):#O(50000)
    pre,next = map(int,sys.stdin.readline().split())
    graph[pre][next] = 1

for midNode in range(1,n+1): #O(400*400*400)
    for startNode in range(1,n+1):
        for endNode in range(1,n+1):
            graph[startNode][endNode] = min(graph[startNode][midNode]+graph[midNode][endNode],graph[startNode][endNode])

trial = int(sys.stdin.readline())

for _ in range(trial): #(50000)
    startN,endN = map(int,sys.stdin.readline().split())
    answer = graph[startN][endN]
    answer2 = graph[endN][startN]
    if(answer == INF and answer2 == INF):
        print(0)
    elif(answer != INF):
        print(-1)
    else: #answer2 != INF #사건의 전후 관계가 모순인 경우는 없다 -> ans과 ans2가 동시에 INF가 아닌경우는 없다
        print(1)

