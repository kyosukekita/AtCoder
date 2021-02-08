N,M=map(int,input().split())
H=list(map(int,input().split()))
AB=[list(map(int,input().split())) for _ in range(M)]

graph=[[0] for _ in range(N)]#はじめに高さ0をいれておく
for i in range(M):
  graph[AB[i][0]-1].append(H[AB[i][1]-1])
  graph[AB[i][1]-1].append(H[AB[i][0]-1])
  
ans=0
for i in range(N):
  if H[i] >max(graph[i]):
    ans+=1
    
print(ans)
