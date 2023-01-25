import sys
import math

n,atk = map(int,sys.stdin.readline().split())

rooms = []
# def trip(rooms,maxHP): #용을 쓰러트리면 True 아니면 False
#     curHP = maxHP
#     curATK = atk
#     for t,a,h in rooms:
#         if(t==1): #몬스터
#             while(True):
#                 h -=curATK #용사의 공격력 HATK만큼 몬스터의 생명력을 깎습니다.
#                 if(h<=0):#몬스터의 생명력이 0 이하이면
#                     break
#                 curHP -= a #몬스터의 공격력만큼 용사의 생명력 HCurHP를 깎습니다.
#                 if(curHP<=0):#용사의 생명력이 0 이하이면
#                     return False #패배
#         else: #포션
#             curATK+=a
#             curHP = min(curHP+h,maxHP)

#     return True #용을 쓰러트림

def trip(rooms,maxHP): #용을 쓰러트리면 True 아니면 False #O(100000)
    curHP = maxHP
    curATK = atk
    for t,a,h in rooms:
        if(t==1): #몬스터
            curHP -= ((math.ceil(h / curATK)-1) * a)
            if(curHP<=0): #용사가 졌을 때
                return False
        else: #포션
            curATK+=a
            curHP = min(curHP+h,maxHP)

    return True #용을 쓰러트림


    

for _ in range(n): #O(100000)
    rooms.append(list(map(int,sys.stdin.readline().split())))

maxMaxHP = int(1e17)
minMaxHP = 1

ansMaxHP =int(1e17+1)
while(minMaxHP<=maxMaxHP): #O(100000log(1e15))
    midMaxHP = (minMaxHP+maxMaxHP)//2
    if(trip(rooms,midMaxHP)): #여행 성공하면
        if(ansMaxHP>midMaxHP): #ans갱신
            ansMaxHP = midMaxHP
        maxMaxHP = midMaxHP-1
    else: #여행 실패하면
        minMaxHP = midMaxHP+1

print(ansMaxHP)


