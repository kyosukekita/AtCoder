N,M,X=map(int,input().split())

C=[]
A=[]
for i in range(N):
  line=list(map(int,input().split()))
  C.append(line[0])
  A.append(line[1:])

ans=float("inf")
for book in range(2**N):
  #その本の組み合わせを選んだ時の合計金額と各理解度
  cost=0
  rikaido=[0 for _ in range(M)]  
  for i in range(N):
    if (book>>i)&1==0:
      cost+=C[i]
      rikaido=[x+y for (x,y) in zip(rikaido, A[i])]
  
  if len([i for i in rikaido if i>=X])==M:
    ans=min(ans,cost)

if ans==float("inf"):
  print(-1)
else:
  print(ans)
