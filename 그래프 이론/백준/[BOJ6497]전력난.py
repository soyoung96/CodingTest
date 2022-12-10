import sys

while(True):
    m,n = map(int,sys.stdin.readline().split())

    if(m == 0 and n == 0):
        break

    totalCost = 0
    minCost = 0
    edgeL = []

    def findRoot(node,rootL):
        if(node != rootL[node]):
            rootL[node] = findRoot(rootL[node],rootL)
        
        return rootL[node]

    def sumNodes(node1,node2,rootL): #합쳐지면 True 아님 False 반환
        root1 = findRoot(node1,rootL)
        root2 = findRoot(node2,rootL)

        if(root1 != root2): #합침
            if(root1<root2):
                rootL[root2] =root1
            else:
                rootL[root1] =root2
            return True
        return False


    for _ in range(n): #200000
        x,y,z = map(int,sys.stdin.readline().split())
        totalCost +=z
        edgeL.append((z,x,y))

    rootL = [ i for i in range(m+1)]

    edgeL.sort() #200000log#200000

    for edge in edgeL: #200000
        z,x,y = edge[0],edge[1],edge[2]
        if(sumNodes(x,y,rootL)):
            minCost+=z

    print(totalCost - minCost)










