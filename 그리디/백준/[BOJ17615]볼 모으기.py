import sys

n = int(sys.stdin.readline())
inputL = list(sys.stdin.readline().rstrip())

#맨 양끝 색깔에서 봤을때
# 색깔 바뀌는 지점 부터 같은 색깔 볼 세서 더 적은 쪽 개수가 답! -> 그리디

cntL=[]
# 왼쪽으로 파란색 옮기기#O(500000)
iscnt = False
cnt =0
for ind in range(len(inputL)):
    elt = inputL[ind]
    if(elt == 'R'):
        iscnt =True
    if(iscnt and elt == 'B'):
        cnt+=1

cntL.append(cnt)

# 왼쪽으로 빨간색 옮기기#O(500000)
iscnt = False
cnt =0
for ind in range(len(inputL)):
    elt = inputL[ind]
    if(elt == 'B'):
        iscnt =True
    if(iscnt and elt == 'R'):
        cnt+=1

cntL.append(cnt)

# 오른쪽으로 빨간색 옮기기#O(500000)
iscnt = False
cnt =0
for ind in range(len(inputL)-1,-1,-1):
    elt = inputL[ind]
    if(elt == 'B'):
        iscnt =True
    if(iscnt and elt == 'R'):
        cnt+=1

cntL.append(cnt)

# 오른쪽으로 파란색 옮기기 #O(500000)
iscnt = False
cnt =0
for ind in range(len(inputL)-1,-1,-1):
    elt = inputL[ind]
    if(elt == 'R'):
        iscnt =True
    if(iscnt and elt == 'B'):
        cnt+=1

cntL.append(cnt)



print(min(cntL))


