# import sys

# n = int(sys.stdin.readline())
# edges=[]
# nodes = []
# for _ in range(n):
#     x,y,z = map(int,sys.stdin.readline().split())
#     nodes.append((x,y,z))

# for start in range(len(nodes)-1):
#     for end in range(start+1,len(nodes)):
#         node1 = nodes[start]
#         node2 = nodes[end]
#         distance = min(abs(node1[0]-node2[0]),abs(node1[1]-node2[1]),abs(node1[2]-node2[2]))
#         edges.append((distance,start,end))

# edges.sort()

# roots=[i for i in range(n)]

# def findroot(roots,node):
#     if(roots[node]!= node):
#         roots[node] = findroot(roots,roots[node])
    
#     return roots[node]

# def union(roots,node1,node2):
#     root1 = findroot(roots,node1)
#     root2 = findroot(roots,node2)
#     if(root1!=root2):
#         if(root1<root2):
#             roots[root2] = root1 #합체
            
#         else:
#             roots[root1] = root2

#         return True
    
#     else:

#         return False
    
# totalCost = 0
# for edge in edges:
#     dist,n1,n2 = edge
#     if(union(roots,n1,n2)):
#         totalCost+=dist

# print(totalCost)

import sys

n = int(sys.stdin.readline())
edges=[]
nodes = []
x=[]
y=[]
z=[]
for node in range(n):#100000
    xv,yv,zv = map(int,sys.stdin.readline().split())
    x.append((xv,node))
    y.append((yv,node))
    z.append((zv,node))

x.sort()#100000
y.sort()#100000
z.sort()#100000

for ind in range(len(x)-1):#100000
    edges.append((x[ind+1][0] - x[ind][0],x[ind][1],x[ind+1][1]))
    edges.append((y[ind+1][0] - y[ind][0],y[ind][1],y[ind+1][1]))
    edges.append((z[ind+1][0] - z[ind][0],z[ind][1],z[ind+1][1]))



edges.sort() #300000log(300000)

roots=[i for i in range(n)]

def findroot(roots,node):
    if(roots[node]!= node):
        roots[node] = findroot(roots,roots[node])
    
    return roots[node]

def union(roots,node1,node2):
    root1 = findroot(roots,node1)
    root2 = findroot(roots,node2)
    if(root1!=root2):
        if(root1<root2):
            roots[root2] = root1 #합체
            
        else:
            roots[root1] = root2

        return True
    
    else:

        return False
    
totalCost = 0
for edge in edges:#300000
    dist,n1,n2 = edge
    if(union(roots,n1,n2)):
        totalCost+=dist

print(totalCost)
    
    



