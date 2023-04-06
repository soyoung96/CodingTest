from collections import Counter
def solution(k, tangerine):
   
    answer = 0
    dic = Counter(tangerine)
   
    canDiscardNum = len(tangerine) -k
   
    sortL = []
   
    dicKeys = list(dic.keys())
   
    for key in dicKeys:
        sortL.append((dic[key],key))
       
    sortL.sort()
   
    minusInd = 0
    sumValue = 0
   
    # print(sortL)
    for ind,(value,key) in enumerate(sortL):
        sumValue+=value
        if(canDiscardNum<sumValue):
            break
        # print(value,key)
        minusInd = ind+1
       
    answer = len(sortL) - minusInd
   
       
    return answer