import sys
from pprint import pprint

h,w = map(int,sys.stdin.readline().split())
# graph = [[0] *(w) for _ in range(h)]

blockLenL = list(map(int,sys.stdin.readline().split()))

# for y in range(w):
#     for x in range(h-1,h-1-blockLenL[y],-1):
#         graph[x][y] = 1


# leftBlock = [-1,-1] #y좌표,길이
# rightBlock = [-1,-1]

# rainMaxH = []

# leftBlock = [-1,-1] #y좌표,길이
# rightBlock = [-1,-1]
# for ind,blockLen in enumerate(blockLenL):
#     if(ind == 0): #첫 시작이면 무조건 leftBlock
#         leftBlock = [ind,blockLen]
#     else:
#         if(blockLen<leftBlock[1]): #왼쪽 블락보다 길이가 작으면
#             if(rightBlock[1]<blockLen): #오른쪽 블락보다 길이가 길면
#                 rightBlock = [ind,blockLen] #오른쪽 블락 갱신
#         else: #왼쪽 블락보다 길이 길면
#             rainMaxH.append((leftBlock[0],ind,leftBlock[1])) #빗물 최대 깊이 정보 추가
#             leftBlock = [ind,blockLen] #왼쪽 블락 갱신
#             rightBlock = [-1,-1] #오른쪽 블락 초기화

# if(rightBlock[0] != -1): #초기화 블록 아닐때
#     rainMaxH.append((leftBlock[0],rightBlock[0],rightBlock[1])) #빗물 최대 깊이 정보 추가

# print(rainMaxH)
# ans =0
# for startInd,endInd,rainMax in rainMaxH:
#     for y in range(startInd+1,endInd):
#         ans+=rainMax-blockLenL[y]

# print(ans)


ans = 0
for i in range(1, w - 1):
    left_max = max(blockLenL[:i])
    right_max = max(blockLenL[i+1:])

    compare = min(left_max, right_max)

    if blockLenL[i] < compare:
        ans += compare - blockLenL[i]

print(ans)
 


    