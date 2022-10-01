import sys
from pprint import pprint

def chkA(a):
    if(0<=a<n):
        return True #안 벗어남
    else:
        return False #범위 벗어남

def chkB(b):
    if(0<=b<m):
        return True #안 벗어남
    else:
        return False #범위 벗어남

def chkD(d):
    if(d<0):
        return 3
    else:
        return d 

n,m = map(int, sys.stdin.readline().split())

a,b,d = map(int, sys.stdin.readline().split())

mapL=[]

for _ in range(n):
    mapL.append(list(map(int,sys.stdin.readline().split())))

da = [-1,0,1,0]
db = [0,1,0,-1] # 북0동1남2서3

final = False
while True:
    if(final):# 끝난거면 반복 탈출
        break
    for tryN in range(4):#4번 시도
        # pprint(mapL)
        # if(input()=="1"):
        #     exit() #디버그 로깅
        d = chkD(d-1) # 이동 실패하면 왼쪽 방향봄
        nextA,nextB = a+da[d],b+db[d]
        if(chkA(nextA)and chkB(nextB)):# 이동하려는 칸이 맵 안에 존재
            if(mapL[nextA][nextB]==0): #아직 안가본 칸 -> 이동가능
                a,b = nextA,nextB #이동
                mapL[a][b]=2
                break # 이동 성공하면 다음 4번의 시도
        #이동 실패시
        if(tryN == 3):#4방향 다 실패
            d = chkD(d-1)
            d = chkD(d-1)#뒤를 향해
            nextA,nextB = a+da[d],b+db[d]#가지만
            d = chkD(d-1)
            d = chkD(d-1)#방향은 그대로
            if(chkA(nextA)and chkB(nextB)):# 이동하려는 칸이 맵 안에 존재
                if(mapL[nextA][nextB]!=1): #바다아님 -> 이동가능
                    a,b = nextA,nextB #이동
                    mapL[a][b]=2
                    break # 이동 성공하면 다음 4번의 시도
            #이동실패시
            final =True #끝냄
            break
        else: #아직 4방향 다 실패 X
            continue

answer = 0

for a in range(n):
    for b in range(m):
        if(mapL[a][b]==2):
            answer+=1

print(answer)
    
            

  

            




