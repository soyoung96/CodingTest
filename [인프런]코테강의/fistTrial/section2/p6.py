# n = int(input())
# inputList = list(map(int,input().split()))


# def digit_sum(x):
#   sumList=[0]*n
#   for i in range(8):
#     decimal = 10**i
#     for j in range(len(x)):
#       sumList[j]+=(x[j]//decimal)
    

#   return sumList

# sumList = digit_sum(inputList)

# max = -1
# maxInd = -1
# for i in range(len(sumList)):
#   if(sumList[i]>max):
#     max = sumList[i]
#     maxInd = i
    
# print(inputList[i])
'''
degit_sum의 의미=> 나처럼 list를 인풋으로 받을 게 아니라
원소 하나를 받아서 다 합치는 함수 만들라는 말이었음

'''
n = int(input())
inputList = list(map(int,input().split()))

def digit_sum(x):
  sum=0
  while(x%10>0):
    sum+=x%10
    x = x//10
  return sum

#파이썬으로 더 간단하게
# def digit_sum(x):
#   sum=0
#   tmp=str(x)
#   for i in range(len(tmp)):
#     sum += int(tmp[i])

#   return sum


max = -1
maxInd = -1
for i in range(n):
  tmpSum=digit_sum(inputList[i])
  if(max<tmpSum):
    max = tmpSum
    maxInd = i

print(inputList[maxInd])

    
      
      
    