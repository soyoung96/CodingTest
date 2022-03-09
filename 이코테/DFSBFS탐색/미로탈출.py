from collections import deque
n,m = map(int,input().split())
inputL = [list(map(int,input())) for _ in range(n)]
dx =[1,0,-1,0]
dy= [0,1,0,-1]

def bfs(start):
  y,x=start[0]-1,start[1]-1
  deq=deque()
  deq.append((y,x))

  while deq:
    y,x=deq.popleft()

    for i in range(4):
      goY,goX = y+dy[i],x+dx[i]
      if(goY>=n or goX>=m or goY<0 or goX<0):
        continue
      elif(inputL[goY][goX]==0):
        continue
      elif(inputL[goY][goX]==1):
        inputL[goY][goX] = inputL[y][x]+1
        deq.append((goY,goX))
  return (inputL[n-1][m-1])

print(bfs((1,1)))

  
  