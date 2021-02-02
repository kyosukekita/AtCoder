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
