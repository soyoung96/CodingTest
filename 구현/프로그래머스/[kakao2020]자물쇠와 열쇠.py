from copy import deepcopy

def spin(key): #오른쪽 90도 회전
    
    m = len(key)
    
    newKey = [[0]*(m) for _ in range(m)]
    
    for x,elt in enumerate(key): #행
        y = m - x - 1 #열
        for eltX,eltElt in enumerate(elt):
            newKey[eltX][y] = eltElt
    
    return newKey

def solution(key, lock):
    answer = False
    
    m = len(key)
    n = len(lock)
    
    tmpLock = [[0] * (2*m+n) for _ in range(2*m+n)]
    
    tmpKey = [[0] * (2*m+n) for _ in range(2*m+n)]
    
    lockKey = [[0] * (2*m+n) for _ in range(2*m+n)]
    
    for x in range(m,m+n):
        for y in range(m,m+n):
            lx = x - m
            ly = y- m
            tmpLock[x][y] = lock[lx][ly]
             
    
    for startKeyindX in range(1,m+n): #1~m+n-1
        for startKeyindY in range(1,m+n): #1~m+n-1
            
            for s in range(4): #4번 회전
                tmpTmpKey = deepcopy(tmpKey)
                tmpLockKey = deepcopy(lockKey)
                key = spin(key)#회전
                for x in range(startKeyindX,startKeyindX+m): #key를 tmpTmpKey에 붙이기
                    for y in range(startKeyindY,startKeyindY+m):
                        kx = x - startKeyindX
                        ky = y - startKeyindY
                        tmpTmpKey[x][y] = key[kx][ky]
                
                for x in range(2*m+n):#키 자물쇠 맞춰보기
                    for y in range(2*m+n):
                        tmpLockKey[x][y] = tmpTmpKey[x][y] + tmpLock[x][y] 
                
                isSolution=True
                for x in range(m,m+n): # 유효한 키 인지 검사
                    for y in range(m,m+n):
                        if(tmpLockKey[x][y] !=1):
                            isSolution = False
                            break
                    if(not isSolution): #sol 이 아니면
                        break #반복 탈출
                        
                if(isSolution):# sol 이면 
                    answer = True #키로 열 수 있음
                    break
            if(answer):
                break
        if(answer):
            break
            
    return answer
        