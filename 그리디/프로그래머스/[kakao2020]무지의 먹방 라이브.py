def solution(food_times, k):
    
    finish = []
    time=0 #소요시간
    s = len(food_times)
    answer = -1
    while(s!=0):
        preK = k
        k-=s
        if(k>=0):
            time+=1
            total =0 #다음턴에서 빠질 음식 수
            
            for ind,food_time in enumerate(food_times):
                if(food_time == time):
                    total+=1
                    food_times[ind]=-1
                
            s-=total
        
        else:
            existFood=0#존재하는 푸드중 지나간 푸드수
            for ind,food_time in enumerate(food_times):
                if(food_time!=-1): #존재하는 푸드
                    if(existFood==preK):
                        answer = ind+1
                        break
                    else:
                        existFood+=1 #존재하는 푸드중 지나간 푸드수 증가
            break
        
    
    return answer