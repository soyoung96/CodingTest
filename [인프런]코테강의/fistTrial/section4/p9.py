'''
1-N 수열
왼수 오른수중 하나 가져와서 가장 길게 증가수열 만듬
-> 가져온 숫자 제거됌
'''
from collections import deque

n = int(input())
inputList=list(map(int,input().split()))
inputQ =deque(inputList)

tmp=-1
prtStr=""
while(len(inputQ)!=0):
  lt =inputQ[0]
  rt = inputQ[-1]
  if(lt<rt): #가장 긴 증가수열 만들기 위해
    if(lt>=tmp): #증가수열인가?
      tmp =inputQ.popleft()
      prtStr+="L"
    elif(rt>=tmp):
      tmp =inputQ.pop()
      prtStr+="R"
    else:
      break # 끝
  else:
    if(rt>=tmp): #증가수열인가?
      tmp =inputQ.pop()
      prtStr+="R"
    elif(lt>=tmp):
      tmp =inputQ.popleft()
      prtStr+="L"
    else:
      break # 끝


print(len(prtStr))
print(prtStr)

      
      
      
      
  