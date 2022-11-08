def chkRight(p): #올바른 문자열인지 확인
    
    sum=0

    for i in p:
        if(i == "("):
            sum+=1
        else:
            sum-=1
        if(sum<0): #올바르지 않은 문자열
            return False
    
    if(sum!=0): #올바르지 않은 문자열
        return False
    else:#올바른 문자열
        return True
        
def reversingP(p):
    
    result=""
    for i in p:
        if(i=="("):
            result+=")"
        elif(i==")"):
            result+="("
    
    return result

def splitP(p): #균형 균형 으로 분리하기
    left = 0
    right = 0
    mid=0
    for ind,i in enumerate(p):
        if(i == "("):
            left+=1
        else:
            right +=1
        if(left == right):
            mid=ind
            break
    
    if(mid+1 <= len(p)):
        result = (p[:mid+1],p[mid+1:])
        
    else: #v는 빈 문자열이 될 수 있습니다.
        result = (p,"")
    
    return result
            

def solution(p):
          
    if(p==""): #입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
        return p
    u,v = splitP(p)#문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    if(chkRight(u)):
        return u + solution(v)#이어붙여서 반환
      
    else:
        tmpAnswer =""
        tmpAnswer+="("#빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        tmpAnswer+=solution(v)#문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어 붙입니다. 
        tmpAnswer+=")"
        tmpAnswer+=reversingP(u[1:len(u)-1])#u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 

        return tmpAnswer
