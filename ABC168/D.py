N,M = map(int, input().split())
AB=[list(map(int,list(input().split()))) for _ in range(M)]

#幅優先探索
#グラフを作成
graph=[[] for _ in range(N)]
for i in range(M):
  graph[AB[i][0]-1].append(AB[i][1]-1)
  graph[AB[i][1]-1].append(AB[i][0]-1)
  
from collections import deque
dist=[-1]*N #dist[i]には頂点1から頂点i+1の最短距離を入れる
dist[0]=0

prev=[-1]*N #prev[i]には、頂点i+1到達直前のノードの番号を入れる

d=deque() #新しく訪問した頂点を末尾に追加するor先頭から過去に訪問した頂点を取り出す
d.append(0)

while d:
  v=d.popleft()
  for i in graph[v]:
    if dist[i]!=-1:#訪問済みであれば
      continue
    dist[i]=dist[v]+1
    prev[i]=v+1
    d.append(i)#今回新しく訪問した頂点iをdの末尾に追加

ans=dist
if -1  in dist:
  print("No")
else:
  print("Yes")
  for i in prev[1:]:
    print(i)
