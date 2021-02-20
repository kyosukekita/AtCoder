N,K = map(int, input().split())

def f(x):
  tmp=[int(i) for i in list(str(x))]
  g1="".join(map(str,sorted(tmp, reverse=True)))
  if g1[0]==0:
    g1=g1[1:]
    
  g2="".join(map(str,sorted(tmp)))
  if g2[0]==0:
    g2=g2[1:]
  return int(g1)-int(g2)

ans=N
for i in range(K):
  ans=f(ans)

print(ans)
