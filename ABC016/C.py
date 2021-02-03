import sys
sys.setrecursionlimit(10**6) #これ設定しないとREエラーになる

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

#グラフを描く
graph=[[] for _ in range(N)]
for edge in edges:
  graph[edge[0]-1].append(edge[1]-1)
  graph[edge[1]-1].append(edge[0]-1)

#答えをいれていくリスト
friends=[0 for _ in range(N)]

for i in range(N):
  tmp=[]
  for j in graph[i]:
    tmp+=[k for k in graph[j] if k!=i and k not in graph[i]]
  
  friends[i]+=len(list(set(tmp)))

for i in range(N):
  print(friends[i])


#別解https://qiita.com/Takayoshi_Makabe/items/65f20edbd970070419f4
n, m = map(int, input().split())
friend = [[100 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    friend[a][b] = 1
    friend[b][a] = 1

for i in range(n):
    friend[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            friend[i][j] = min(friend[i][j], friend[i][k]+friend[k][j])
            # ダイクストラ法
            # iからjに直接行くよりもkを経由した方が近い場合、iとjの距離を更新

for m in range(n):
    print(friend[m].count(2))
    # 最終的に距離が2の関係がいくつあるかを出力
