'''
중복허용 x-> set이용
안겹치게 뽑기 아래와 같은 for문 이용
'''
n,k = map(int,input().split())
cards=list(map(int,input().split()))

allSum = set()
for i in range(n):
  for i1 in range(i+1,n):
    for i2 in range(i1+1,n):
      allSum.add(cards[i]+cards[i1]+cards[i2])

rankSum = sorted(list(allSum),reverse=True)

print(rankSum[k-1])
  
      


