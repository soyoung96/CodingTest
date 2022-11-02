def solution(N, stages):
    
    failNumL = [0] * (N+1)
    
    
    for stage in stages:
        failNumL[stage-1] += 1 # 실패한 사람 추가
    
    for start in range(N+1):
        if(sum(failNumL[start:])!=0):
            failNumL[start]/=sum(failNumL[start:]) # 실패율 구하기
        else:
            failNumL[start] = 0 #스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
    
    teamfailNumL=[]
    for team,failNum in enumerate(failNumL):
        teamfailNumL.append([team+1,failNum])
        
    teamfailNumL.pop() # 마지막 다 통과할 경우의 레벨은 실패율 안따지므로 빼줌
    
    teamfailNumL.sort(reverse = True,key = lambda x:x[1])
    
    answer = []
    
    for team,_ in teamfailNumL:
        answer.append(team)
        
    return answer