n,m = map(int,input().split())
inputL =[list(map(int,input())) for _ in range(n)]
#인접행렬/인접리스트 아님-> 이거 자체가 방문 했냐 안했냐 나타냄
# -> visited 굳이 표시x
cnt =0

def dfs(y,x):
  if(not((y>=0 and y<n) and(x>=0 and x<m))):
    return False
  else:
    if(inputL[y][x]==0):
      inputL[y][x]=1
      dfs(y+1,x)
      dfs(y-1,x)
      dfs(y,x+1)
      dfs(y,x-1)

for i in range(n):
  for j in range(m):
    if(inputL[i][j]==0):
      cnt+=1
      dfs(i,j)

print(cnt)