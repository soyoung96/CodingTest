import sys
import heapq

n = int(sys.stdin.readline())


roomNum = 0

eachRoomLastTime = []

classes = []
for _ in range(n): #200000
    s,t = map(int,sys.stdin.readline().split())
    classes.append((s,t))

classes.sort() #200000log200000

for ind,(s,t) in enumerate(classes): #200000 log 200000
    if(ind == 0):
        roomNum+=1 #방 증가
        heapq.heappush(eachRoomLastTime,t)
    else:
        if(s>=eachRoomLastTime[0]): # 수업을 배정할 수 있는 방 있음
            heapq.heappop(eachRoomLastTime) #last time 이 최신 수업last time으로 갱신
            heapq.heappush(eachRoomLastTime,t)#last time 이 최신 수업last time으로 갱신
        else: # 수업을 배정할 수 있는 방이 없음
            roomNum+=1 #방증가
            heapq.heappush(eachRoomLastTime,t)

print(roomNum)

    

    

    
    
    










