inputList = [list(map(int,input().split()))for _ in range(7)]

cnt =0
for y in range(7):
  tmp=list()
  for x in range(7-5+1):
    e1,e2,e4,e5 = inputList[y][x],inputList[y][x+1],inputList[y][x+3],inputList[y][x+4]
    d1,d2,d4,d5 = inputList[x][y],inputList[x+1][y],inputList[x+3][y],inputList[x+4][y]

    if(e1==e5 and e2==e4):
      cnt+=1
    if(d1==d5 and d2==d4):
      cnt+=1

print(cnt)
    
    
    