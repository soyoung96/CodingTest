def chkYX(yx,n):# 그래프의 높이를 벗어나는지
    if(0<=yx<=n):
        return True
    else:
        return False

def chkB(y,x,graph):
    if(y != 0):#한쪽 끝 부분이 기둥 위에 있거나
        if(0 in graph[y-1][x]): #보의 왼쪽
            return True
        else:
            if((x+1)<len(graph)):
                if(0 in graph[y-1][x+1]): #보의 오른쪽
                    return True
    if(0<x<len(graph)-1): #양쪽 끝 부분이 다른 보와 동시에 연결
        if(1 in graph[y][x-1] and 1 in graph[y][x+1]):
            return True
                 
    return False
           
    
def chkG(y,x,graph):
    if(y==0):#기둥은 바닥 위에 있거나
        return True
    if(1 in graph[y][x]):#보의 왼쪽 끝 부분 위에 있거나
        return True
    if(x!=0):#보의 오른쪽 끝 부분 위에 있거나
        if(1 in graph[y][x-1]):
            return True
    if(y!=0):#또는 다른 기둥 위에 있어야 합니다.
        if(0 in graph[y-1][x]):
            return True
        
    return False
    
def setB(y,x,graph): #보를 지음
    if(chkYX(x+1,len(graph))):#보를 지어도 그래프 안
        if(chkB(y,x,graph)): 
            graph[y][x].append(1) #보를 지음
            

def setG(y,x,graph): #기둥을 지음
    if(chkYX(y+1,len(graph))):#기둥을 지어도 그래프 안
        if(chkG(y,x,graph)): 
            graph[y][x].append(0) #기둥을 지음

def delB(y,x,graph): #보를 없애
    graph[y][x].pop(graph[y][x].index(1)) #보를 없애봄
    noChance = False
    for tmpX in range(len(graph)):
        for tmpY in range(len(graph)):
            for i in graph[tmpY][tmpX]:
                if(i == 0): #기둥이라면
                    if(not chkG(tmpY,tmpX,graph)):
                        
                        noChance = True
                        break
                else: #보 라면
                    if(not chkB(tmpY,tmpX,graph)):
                        noChance = True
                        break
                        
            if(noChance):
                break
        if(noChance):
            break
    if(noChance): #없앨 수 없음 복구
        graph[y][x].append(1)
        
def delG(y,x,graph): #기둥을 없애
    graph[y][x].pop(graph[y][x].index(0)) #기둥를 없애봄
    noChance = False
    for tmpX in range(len(graph)):
        for tmpY in range(len(graph)):
            for i in graph[tmpY][tmpX]:
                if(i == 0): #기둥이라면
                    if(not chkG(tmpY,tmpX,graph)):
                        noChance = True
                        break
                else: #보 라면
                    if(not chkB(tmpY,tmpX,graph)):
                        noChance = True
                        break
                        
            if(noChance):
                break
        if(noChance):
            break
    if(noChance): #없앨 수 없음 복구
        graph[y][x].append(0)



def solution(n, build_frame):
    graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
    
    print(graph)
    for build in build_frame:
        x,y,a,b = build[0],build[1],build[2],build[3]
        if(a==0 and b==0): #기둥 삭제
            delG(y,x,graph)
        if(a==0 and b==1): #기둥 설치
            setG(y,x,graph)     
        if(a==1 and b==0): #보 삭제
            delB(y,x,graph)
        if(a==1 and b==1): #보 설치
            setB(y,x,graph) 

    answer = []
    
    for tmpX in range(len(graph)):
        for tmpY in range(len(graph)):

            graph[tmpY][tmpX].sort()
            for elt in graph[tmpY][tmpX]:
                answer.append([tmpX,tmpY,elt])
        
    
    return answer