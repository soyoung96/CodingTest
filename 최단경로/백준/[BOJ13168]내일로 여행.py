import sys
from pprint import pprint
INF = int(1e10)
n,r = map(int,sys.stdin.readline().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
graph2 = [[INF] * (n+1) for _ in range(n+1)]

inputL = list(sys.stdin.readline().rstrip().split())
dictionary = dict()
for ind,inputE in enumerate(inputL):
    dictionary[inputE] = ind+1

m = int(sys.stdin.readline())
inputL2 = list(map(lambda x: dictionary[x],sys.stdin.readline().rstrip().split()))

k = int(sys.stdin.readline())

discounts0 = {"Mugunghwa","ITX-Saemaeul","ITX-Cheongchun"}
discounts = {"S-Train","V-Train"}

for i in range(1,n+1):
    graph[i][i] =0
    graph2[i][i] = 0

for _  in range(k):
    trans,start,end,money = sys.stdin.readline().split()
    money = int(money)
    start = dictionary[start]
    end = dictionary[end]
    if(trans in discounts0):
        graph2[start][end] = 0
        graph2[end][start] = 0
    elif(trans in discounts):
        if(money/2<graph2[start][end]):
            graph2[start][end] = money/2
            graph2[end][start] = money/2
    else:
        if(money<graph2[start][end]):
            graph2[start][end] = money
            graph2[end][start] = money

    if(money<graph[start][end]):
        graph[start][end] = money
        graph[end][start] = money



for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            graph[start][end] = min(graph[start][mid] + graph[mid][end],graph[start][end])
            graph2[start][end] = min(graph2[start][mid] + graph2[mid][end],graph2[start][end])

cost1 = 0
cost2 = 0

# pprint(graph)
# pprint(graph2)
for i in range(m-1):
    start = inputL2[i]
    end =  inputL2[i+1]
    # print(graph[start][end])
    # print(graph2[start][end])
    cost1 += graph[start][end]
    cost2 += graph2[start][end]

# print(cost1)
# print(cost2+r)
if(cost1>cost2+r):
    print("Yes")
else:
    print("No")

    

    






