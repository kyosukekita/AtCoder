#周囲の4マスのうち、#が奇数個存在するとき、その点が多角形の頂点
H,W=map(int,input().split())
S=[input() for _ in range(H)]
ans=0
for h in range(1,H):
  for w in range(1,W):
    cnt=0
    for i in range(2):
      for j in range(2):
        if S[h-i][w-j]=="#":
          cnt+=1
    if cnt%2==1:
      ans+=1
print(ans)
