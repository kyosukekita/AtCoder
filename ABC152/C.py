N=int(input())
P=list(map(int, input().split()))

ans=1
minimum=P[0]

for i in range(1,N):
  if P[i]<=minimum:
    ans+=1
    minimum=P[i]
  else:
    pass
print(ans)   
