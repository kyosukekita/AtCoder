n, m = map(int, input().split())
cnt = [[] for _ in range(n + 1)]#index iにはi県に属している市が書き込まれる

for i in range(m):
    p, y = map(int, input().split())
    cnt[p].append([y, i])
     
buf = [-1] * m
for i in range(len(cnt)):
    if not cnt[i]:
        continue
    cnt[i].sort()
    for j in range(len(cnt[i])):
        buf[cnt[i][j][1]] = '{:06d}{:06d}'.format(i, j + 1)#または、str("1").zfill(6)で000001となる。
print('\n'.join(buf))
