from collections import deque

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append(b)
    edge[b].append(a)

ans = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    ans[p-1] += x

q = deque()
q.append(0)
check = [False] * N
 
while q:
    v = q.pop()
    check[v] = True
    for u in edge[v]:
        if check[u] == True:
            continue
        ans[u] += ans[v]
        q.append(u)

print(*ans)




#TLE &WA
from collections import deque
N,Q = map(int, input().split())
edges=[list(map(int,list(input().split()))) for _ in range(N-1)]
operation=[list(map(int,list(input().split()))) for _ in range(Q)]

graph=[[] for _ in range(N)]
for edge in edges:
  graph[edge[0]-1].append(edge[1]-1)

counter=[0]*N
def dfs(graph,start,count):
  visited=[]
  stack=deque()
  stack.append(start)
  while len(stack)>0:
    next_node=stack.pop()#リストのpopと違って、pop(-1)ができない
    if next_node in visited:
      continue
    visited.append(next_node)
    counter[next_node]+=count
    for nei in graph[next_node]:
      stack.append(nei)

for j in range(Q):
  dfs(graph,operation[j][0]-1,operation[j][1])

print(' '.join(map(str,counter)))
