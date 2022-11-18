def solution(files):
    
    tmpFiles = []
    for ind,file in enumerate(files):
        num = ""
        header = ""
        isHeader=True
        isNum = True
        numNum =0
        for s in file:
            
            if((isHeader)and (not s.isdigit())):
                header+=s.lower()
            
            if(isNum and s.isdigit()):
                isHeader = False
                num+=s
                numNum+=1
            if(numNum>0 and (not s.isdigit())):
                isNum = False
                
        tmpFiles.append([header,int(num),ind,file])
        
    tmpFiles.sort(key = lambda x:(x[0],x[1],x[2]))
    print(tmpFiles)
    
    answer = []
    for file in tmpFiles:
        answer.append(file[3])
        
    
    return answer