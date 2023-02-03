import sys

n,k = map(int,sys.stdin.readline().split())

inputL = list(map(int,sys.stdin.readline().split())) #100

belt = []

for elt in inputL:#100
    belt.append([elt,False]) #(내구도,로봇유무) 

def move(belt): #100 #컨베이어벨트 움직임
    tmp = belt[-1]
    belt = [tmp]+belt[:len(belt)-1] 
    return belt

# def findRightRobot(belt): #가장 먼저 실은 로봇위치 반환 #100
#     for ind in range(len(belt)-1,-1,-1):
#         if(belt[ind][1]): #로봇이 있다면
#             return ind
#     return -1 #로봇이 없다면

def getNumDuration0(belt): #내구성 0인 개수 반환
    num =0
    for elt,_ in belt:
        if(elt==0): 
            num+=1
    return num

ans = 0
while(True):
    ans+=1
    belt = move(belt) #벨트 움직임
    if(belt[n-1][1]): #내리는 자리에 로봇있으면
        belt[n-1][1] = False #내려줌
    for ind in range(len(belt)-1,-1,-1):
        if(belt[ind][1]): #로봇이 있고 
            if(belt[ind+1][0]>=1 and (not belt[ind+1][1])):#이동할 곳이 내구성이 1이상 남아있고 로봇 없으면
                belt[ind][1] = False #기존 로봇자리 비우고
                belt[ind+1][1] = True #다음에 로봇 들어감
                belt[ind+1][0]-=1 #다음칸 내구도 감소
                if(belt[n-1][1]): #내리는 자리에 로봇있으면
                    belt[n-1][1] = False #내려줌
    if(belt[0][0]!=0): #올리는 위치에 있는 칸의 내구도가 0이 아니면
        belt[0][1] = True #로봇 올림
        belt[0][0]-=1 #내구도 감소
    
    if(getNumDuration0(belt)>=k):#내구도가 0인 칸의 개수가 K개 이상이면
        break
    

print(ans)   
            




    
