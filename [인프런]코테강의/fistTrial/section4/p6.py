'''
키 몸무게

매 단계 마다 가장 키가 큰사람과 가장 몸무계가 많이 나가는 사람은 뽑힌다.
->키와 몸무게 기준이 정해짐
키 > or  몸무게 >
키 <= and 몸무게<=
'''

n = int(input())
inputList=[list(map(int,input().split())) for _ in range(n)]
inputList.sort(key= lambda x:x[0],reverse=True)
# 사실 위의 키값이 이미 index[0]을 가르키고 있기 때문에
# 키값 안적어 넣어도 된다.

cnt=0
kg=0
for i in range(n):
  if(inputList[i][1]>kg):
    cnt+=1
    kg = inputList[i][1]


print(cnt)
