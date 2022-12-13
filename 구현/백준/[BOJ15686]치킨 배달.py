import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())
INF = int(1e11)
graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

chickens = [] #치킨집 위치
houses = [] #집 위치
for x in range(n):
    for y in range(n):
        if(graph[x][y] == 2): #치킨집이면
            chickens.append((x,y))
        if(graph[x][y] == 1): #집이라면
            houses.append((x,y))

minChickenDist = INF
for mchickens in combinations(chickens,m): #지을 치킨집 선정 #312
    chickenDist = 0
    for x,y in houses: #100 #각 집마다 가장 짧은 치킨집 거리 구하기
        minDist = INF
        for chicken in mchickens:#지은 치킨집 중 #13
            dist = abs(chicken[0] - x) + abs(chicken[1] - y) #거리가
            if(minDist>dist):#가장 짧으면 갱신
                minDist = dist
        chickenDist+=minDist
    if(minChickenDist>chickenDist): #가장 짧은 치킨거리라면 갱신
        minChickenDist = chickenDist

print(minChickenDist)

