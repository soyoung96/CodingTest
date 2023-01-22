import sys
from collections import deque
'''
다익스트라대신 BFS이용한 이유 -> 모든 정점까지의 거리를 구하는게 아니므로!
'''
n,k = map(int,sys.stdin.readline().split())
MAX = 100000
queue = deque([(n,0)])
distL = [-1 for _ in range(MAX+1)]

while(queue): #BFS
    newN,newT = queue.popleft() #수빈이 현재위치
    distL[newN] = newT #시간등록 및 방문
    if(newN == k): #수빈이가 동생잡았을 때
        break
    else:
        if(2*newN<=MAX and distL[2*newN] == -1):
            queue.appendleft((2*newN,newT)) #비용O-> 큐 앞에 배치
        if(0<=newN-1 and distL[newN-1] == -1):
            queue.append((newN-1,newT+1))#비용X-> 큐 뒤에 배치
        if(newN+1<=MAX and distL[newN+1] == -1):
            queue.append((newN+1,newT+1))#비용X-> 큐 뒤에 배치


print(distL[k])

        
            

    




