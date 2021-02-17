#言われた通りに

N,M,T = map(int, input().split())
AB=[list(map(int,list(input().split()))) for _ in range(M)]
AB.insert(0,[0,0])
youryo=N

ans=True
for i in range(1,M+1):
  N-=(AB[i][0]-AB[i-1][1])
  if N<=0:
    ans=False
    break
  N+=(AB[i][1]-AB[i][0])
  N=min(youryo,N)

N-=(T-AB[M][1])

if N<=0:
  ans=False


if ans:
  print("Yes")
else:
  print("No")
