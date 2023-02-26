from collections import deque
def solution(people, limit):
    answer = 0

    people.sort(reverse = True)
    
    people = deque(people)
    
    while(people):
        if(len(people)>=2):
            if(people[0]+people[-1]<=limit):
                answer+=1
                people.popleft()
                people.pop()
            else:
                answer+=1
                people.popleft()
        else:
            answer+=1
            people.popleft()
                
    
    
    return answer