import sys

n = int(sys.stdin.readline())

graph = []
dpGraph = []

for _ in range(n):
    inputL = list(map(int,sys.stdin.readline().split()))
    graph.append(inputL)
    dpGraph.append([-1]*(len(inputL)))

for h in range(n):
    if(h == 0):
        dpGraph[h][0] = graph[h][0]
    else:
        for w in range(len(dpGraph[h])):
            if(w == 0):
                dpGraph[h][w] = graph[h][w]+dpGraph[h-1][w]
            elif(w == (len(dpGraph[h]) -1)):
                dpGraph[h][w] = graph[h][w]+dpGraph[h-1][w-1]
            else:
                dpGraph[h][w] = graph[h][w]+max(dpGraph[h-1][w],dpGraph[h-1][w-1])
        
print(max(dpGraph[-1]))