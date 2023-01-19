import sys
import heapq

n = int(sys.stdin.readline())

k = int(sys.stdin.readline())

sensors=list(map(int,sys.stdin.readline().split()))

sensors.sort() #O(10000log10000)

maxSensor = sensors[-1]
minSensor = sensors[0]

priorQ = []

preSensor = -1

for ind,sensor in enumerate(sensors): #O(10000log1000)
    if(ind != 0):
        heapq.heappush(priorQ,sensor-preSensor)
        if(len(priorQ)>=k):
            heapq.heappop(priorQ)
    preSensor = sensor


print(maxSensor - minSensor - (sum(priorQ)))
        



