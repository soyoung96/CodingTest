# import bisect

# def makeStartEnd(query): #query의 문자열 시작위치 끝위치 반환
    
#     start = -1
#     end = -1
#     isAlpha = True
    
#     if(query[0] == "?"):
#         if(query[-1] == "?"):
#             isAlpha = False
#             return (isAlpha,start,end)
            
#         start = -1
#         tmpStart  = 0 #start를 구하기 위함
#         tmpEnd = len(query)-1 #start를 구하기 위함 -> ?가 가장 end 쪽에 있는 값 찾기
#         end = len(query) -1
#         while(tmpStart<=tmpEnd):
#             mid = (tmpStart+tmpEnd)//2
#             if(query[mid] == "?"): #오른쪽으로 이동가능
#                 tmpStart = mid +1
#             else:                
#                 tmpEnd = mid -1 
#                 start = mid
        
    
#     else:
#         start = 0
#         tmpStart  = 0 #end를 구하기 위함
#         tmpEnd = len(query)-1 #end를 구하기 위함 -> start 전
#         end = -1
#         while(tmpStart<=tmpEnd):
#             mid = (tmpStart+tmpEnd)//2
#             if(query[mid] == "?"): #왼쪽으로 이동가능
                
#                 tmpEnd = mid -1
#             else:
#                 tmpStart = mid +1
#                 end = mid
            
    
#     return (isAlpha,start,end)
            
            

# def isRight(word,query): #쿼리로 word 검색 가능하면 True반환 아님 Flase
    
#     if(len(word)!= len(query)):
#         return False
#     else:
#         isAlpha,start,end = makeStartEnd(query)
#         if(not isAlpha):#전체가 ?이므로 무조건 true
#             return True
#         else:
#             if(word[start:end+1] == query[start:end+1]):
#                 return True
#             else:
#                 return False
            

# def solution(words, queries):
#     answer = []
    
#     for query in queries:
#         sum =0
#         for word in words:
#             if(isRight(word,query)): #쿼리로 word 검색 가능하면
#                 sum+=1
#         answer.append(sum)
    
#     return answer

import bisect


def solution(words, queries):
    answer = []
    
    sameLenwords=[[] for _ in range(10001)]
    
    reverseSameLenwords=[[] for _ in range(10001)]
    
    for word in words: #O(1000000000)
        sameLenwords[len(word)].append(word)
        reverseSameLenwords[len(word)].append(word[::-1])
        
    for sameLenwordsElt in sameLenwords:#O(100000log100000)
        sameLenwordsElt.sort()
        
    for reverseSameLenwordsElt in reverseSameLenwords:#O(100000log100000)
        reverseSameLenwordsElt.sort()
        

    for query in queries: #(100000log100000)
        # answer.append(getRightNum(sameLenwords[len(query)],query)#O(log100000))
        if(query[0] != "?"): # dd??
            answer.append(bisect.bisect_right(sameLenwords[len(query)],query.replace("?","z")) - bisect.bisect_left(sameLenwords[len(query)],query.replace("?","a")))
        else:
            answer.append(bisect.bisect_right(reverseSameLenwords[len(query)],query[::-1].replace("?","z")) - bisect.bisect_left(reverseSameLenwords[len(query)],query[::-1].replace("?","a")))
    

    return answer

        
        

