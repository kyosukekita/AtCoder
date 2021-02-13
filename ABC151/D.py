from collections import deque

def bfs(maze,sy,sx):
  visited=[[-1]*W for j in range(H)]
  res=0
  queue=deque([[sy,sx]])
  visited[sy][sx]=0
  while queue:
    y,x=queue.popleft()
    res=max(res, visited[y][x])
    for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
      new_y,new_x=y+j, x+k
      if new_y >=0 and new_y<H and new_x>=0 and new_x <W:
        if maze[new_y][new_x]=="." and visited[new_y][new_x]==-1:
          visited[new_y][new_x] = visited[y][x]+1
          queue.append([new_y,new_x])
  
  return res

H,W=map(int,input().split())
maze=[input() for i in range(H)]

answer=0
for sy in range(H):
  for sx in range(W):
    if maze[sy][sx]==".":
      tmp=bfs(maze, sy, sx)
      answer=max(answer,tmp)
print(answer)





#TLE
from collections import deque

def bfs(maze,visited,sy,sx,gy,gx):
  queue=deque([[sy,sx]])
  visited[sy][sx]=0
  while queue:
    y,x=queue.popleft()
    if [y,x]==[gy,gx]:
      return visited[y][x]
    for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
      new_y,new_x=y+j, x+k
      if new_y >=0 and new_y<H and new_x>=0 and new_x <W:
        if maze[new_y][new_x]=="." :#and visited[new_y][new_x]==-1:
          visited[new_y][new_x] = visited[y][x]+1
          queue.append([new_y,new_x])

H,W=map(int,input().split())
maze=[input() for i in range(H)]
visited=[[-1]*W for j in range(H)]

answer=0
for sy in range(H):
  for sx in range(W):
    for gy in range(H):
      for gx in range(W):
        if maze[sy][sx]=="." and maze[gy][gx]==".":
          tmp=bfs(maze, visited, sy, sx, gy, gx)
          answer=max(answer,tmp)
print(answer)
