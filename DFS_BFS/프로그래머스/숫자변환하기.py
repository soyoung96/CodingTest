from collections import deque
def solution(x, y, n):
    answer = 0
    visitedL = [-1 for _ in range(y+1)]
    q = deque([])
    q.append((x,0))
    visitedL[x] = 0 #방문
    while(q):
        node,preResult = q.popleft()
        for newNode in (node + n,node * 2,node * 3): #3way 연산
            if(newNode <= y):
                if(visitedL[newNode] == -1): #방문 안한곳이라면
                    q.append((newNode,preResult+1))
                    visitedL[newNode] = preResult+1 #방문 #같은 단계에서 중복 안되게끔 여기다가 반복
   
   
    return visitedL[y]