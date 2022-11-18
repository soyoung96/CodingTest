def solution(n, times):
    
    start = 0
    end = int(1e18)
    
    times.sort()
    
    minT = int(1e18)
    
    while(start<=end):
        peaplenum = 0
        mid = (start + end)//2
        goL = False
        
        for time in times:
            peaplenum+=(mid//time)
            if(peaplenum>=n):
                goL = True
                break
        
        if(goL): #더 최소로 줄일수 있음
            end = mid-1
            if(minT>mid):
                minT = mid
                print(mid)
        else: #어쩔 수 없이 늘려야..
            start = mid+1
    
    answer = minT
            
                
            
                
    
    return answer