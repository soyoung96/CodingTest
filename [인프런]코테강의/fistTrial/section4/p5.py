'''
그리디 알고리즘
-> 각 단계에서 가장 좋은 걸 취한다
-> 가장 좋은건 어떤거?-> 정렬!!!!!!!!

그리디==각 단계가 진행되도 문제의 본질은 바뀌면 안됌
'''

n = int(input())
inputList =[list(map(int,input().split())) for _ in range(n)]

inputList.sort(key = lambda x:x[1])

cnt=0
end = -10
for i in inputList:
  if(i[0]<end):
    continue
  else:
    cnt+=1
    end=i[1]

print(cnt)
