import sys

g = int(sys.stdin.readline()) #탑승구 개수
p = int(sys.stdin.readline()) #비행기 개수


rootL = [ i for i in range(g+1)]

def findRoot(rootL,i):
    if(rootL[i]!=i):
        rootL[i] = findRoot(rootL,rootL[i])
    return rootL[i]
    
def unionNode(a,b):
    rootA = findRoot(rootL,a)
    rootB = findRoot(rootL,b)
    if(rootA != rootB): #union 시켜준다
        if(rootA<rootB):
            rootL[b] = rootA
        else:
            rootL[a] = rootB
    
answer =0

landL = []
for _ in range(p):
    landL.append(int(sys.stdin.readline())) #착륙지

for land in landL:    
    if(findRoot(rootL,land) == 0):
        break
    else:
        unionNode(land,findRoot(rootL,land)-1) #비행기 착륙하고 다음 착륙지 가리키기
        answer+=1

print(answer)






