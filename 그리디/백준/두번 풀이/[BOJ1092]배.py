import sys

n = int(sys.stdin.readline()) #50 #9 8 6
crainL = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline()) #10000
boxL = list(map(int,sys.stdin.readline().split()))

crainL.sort(reverse=True)#9 8 6 
# print(crainL)
boxL.sort() #2 2 7 9 9
# print(boxL)

ans = 0
num = 0
while(boxL):
    isAnsMinus = False
    delL = []
    # num+=1
    # if(num == 4):
    #     break
    # print(boxL)
    for cind,crain in enumerate(crainL):
        if(len(delL)==0):
            lenBoxL = len(boxL)
        else:
            lenBoxL = delL[-1]
        for bind in range(lenBoxL-1,-1,-1):
            if(cind == 0): # 첫번째 크레인일때
                if(boxL[bind]>crain): # 첫번째 크레인 못들때
                    isAnsMinus = True #반복 아예 종료
                    ans = -1
                    break
            if(boxL[bind]<=crain): #들 수 있을 때
                # print(crain,bind)
                delL.append(bind) #해당 짐 삭제
                break       
        if(isAnsMinus):
            break
    if(isAnsMinus):
        break
    # print(delL)
    for delE in delL:
        # print(delE)
        boxL.pop(delE)
    ans +=1 

print(ans)




        
