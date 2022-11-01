def solution(s):
    lenS = len(s)
    
    answers =[]
    
    if(lenS==1): #이것만 아래 for문 예외
        return 1
    for cut in range(1,(lenS//2)+1):
        tmpAnswer =""
        same=1
        prev = s[:cut]
        for step in range(cut,len(s),cut):
            next = s[step:step+cut]
            if(prev == next):
                same+=1
            else:
                if(same>1):#기록
                    tmpAnswer+= (str(same)+prev)
                else:
                    tmpAnswer+=prev
                
                prev = next
                same =1
                
        #남은거 처리
        if(same>1):#기록
            tmpAnswer+= (str(same)+prev)
        else:
            tmpAnswer+=prev
                
        answers.append(tmpAnswer)
    
    
    answer = min(answers,key = lambda x:len(x))
    
    
    return len(answer)
    