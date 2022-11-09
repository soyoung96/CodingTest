# import sys

# n = int(sys.stdin.readline())
# cardL =[] #10^5
# for i in range(n): #O(n)
#     cardL.append(int(sys.stdin.readline()))

# cardL.sort() #O(nlogn)
# answer = 0
# total = 0 #지금까지 묶음 카드 수

# plusL = []
# for ind,card in enumerate(cardL): #O(n) -> 잘못됌! 

#     total+=card
#     if(ind!=0):-> 잘못됌! 
#         answer+=total

# if(n==1):
#     answer =cardL[0]


# print(answer)

import sys
import heapq

n = int(sys.stdin.readline())
cardL =[] #10^5
for i in range(n):#O(nlogn)
    heapq.heappush(cardL,int(sys.stdin.readline()))

total = 0

while(len(cardL)>=2):
    first = heapq.heappop(cardL)
    second = heapq.heappop(cardL)
    total+=(first + second) #비교
    heapq.heappush(cardL,first + second)


print(total)

        

