import sys

n,c = map(int,sys.stdin.readline().split())

house = []

for _ in range(n):
    house.append(int(sys.stdin.readline()))


house.sort()

maxHouse = house[-1]
minHouse = house[0]

def numHouse(house,mid): #가장 인접한 거리가 mid일때 와이파이 최대 갯수
    
    houseNum = 1  #와피파이 설치한 집 수

    visitHouse = house[0] #와이파이 설치한 집
    nextDist = visitHouse +mid # 방문한 집에서 거리 만큼 지났을때
    for nextHouse in house:        
        if(nextHouse>=nextDist):
            houseNum+=1 #와피파이 설치한 집 수 추가
            visitHouse = nextHouse #새로 와피파이 설치한 집
            nextDist = visitHouse +mid # 방문한 집에서 거리 만큼 지났을때 갱신
    
    return houseNum

start = 1 #가장 인접한거리의 최소
end = maxHouse -minHouse #가장 인접한거리의 거리

answer = -1
while (start<=end):
    mid = (start + end)//2

    if(numHouse(house,mid) >= c): # 이 거리 가능 -> 더 거리 늘려도 된다

        # print("mid:"+str(mid))
        # print("numHouse(house,mid):"+str(numHouse(house,mid)))

        if(answer<mid):#가능한 거리 중 최댓값 찾기
            answer = mid 
        start = mid+1
    else:# 어쩔 수 없다.. 거리 줄여야함
        end = mid -1

print(answer)

    

        



