def solution(s):
    answer = []
    dic = dict([])
    for ind,se in enumerate(s):
        if(se not in dic):
            answer.append(-1)
        else: # 이전에 나옴
            answer.append(ind - dic[se])
        dic[se] = ind
       
    return answer