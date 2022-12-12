import sys

n,k = map(int,sys.stdin.readline().split())

inputL = list(map(int,sys.stdin.readline().split()))

muticoncept = set([])
answer =0

for ind in range(len(inputL)): #100
    inputE = inputL[ind]
    if(inputE not in muticoncept): #꼽아야함
        if(len(muticoncept) == n): #꽉 찼으면 뽑아야함 -> 있는 것 중 가장 거리가 먼걸
            if(ind+1<len(inputL)):
                maxMuticonceptE = -1
                maxMuticonceptEDist = -1
                for muticonceptE in muticoncept: #100
                    if(muticonceptE in inputL[ind+1:]):#100
                        muticonceptEDist = inputL[ind+1:].index(muticonceptE) 
                        if(maxMuticonceptEDist<muticonceptEDist):
                            maxMuticonceptEDist = muticonceptEDist
                            maxMuticonceptE = muticonceptE
                    else: #만일 아예 뒤에 안오면 바로 가장 거리가 먼 것 당첨
                        maxMuticonceptE = muticonceptE
                        break
                muticoncept.remove(maxMuticonceptE) #기존 콘셉트 제거                
                answer+=1
                muticoncept.add(inputE)#그 자리에 새로 꼽음
            else:#inputL의 마지막 원소라면
                answer+=1 #걍 아무거나 뻄
                
        else: # 꽉 안찼으면 아무데나 집어넣음
            muticoncept.add(inputE)

print(answer)




            



