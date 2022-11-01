import sys

s = list(map(int,list(sys.stdin.readline().rstrip())))


answer1 = 0
isCount1=True # true 면 센다
for elt in s:
    if(elt == 1 and isCount1):
        answer1+=1
        isCount1 = False
    elif(elt==0): #0이 나오면
        isCount1 = True # 하나의 1구간이 끝나서 다음에 1이 올땐 새로운 구간이라고 보고 세어줌

answer0 = 0
isCount0=True # true 면 센다
for elt in s:
    
    if(elt == 0 and isCount0):
        answer0+=1
        isCount0 = False
    elif(elt==1): #1이 나오면
        isCount0 = True # 하나의 0구간이 끝나서 다음에 0이 올땐 새로운 구간이라고 보고 세어줌

if(answer1>answer0):
    print(answer0)
else:
    print(answer1)
       



