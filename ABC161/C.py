N,K=map(int,input().split())
if N>=K:
  tmp=N//K
  N-=tmp*K
  print(min(N,abs(N-K)))
else:
  print(min(K-N,N))
