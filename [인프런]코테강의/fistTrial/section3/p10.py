sdoku = [list(map(int,input().split())) for _ in range(9)]

def check(sdoku):
  for y in range(9):
    chk1=[0]*10
    chk2=[0]*10
    for x in range(9):
      chk1[sdoku[y][x]]=1
      chk2[sdoku[x][y]]=1
    if(sum(chk1)!=9 or sum(chk2)!=9):
      return False

  for i in range(3):
    for j in range(3):
      chk3 = [0]*10 #0
      for p in range(3):
        for q in range(3):
          chk3[sdoku[3*i+p][3*j+q]]=1

      if(sum(chk3)!=9):
        return False

  return True


if(check(sdoku)):
  print("YES")
else:
  print("NO")