T=int(input())
case=[list(map(int,list(input().split()))) for _ in range(T)]

#累積和
K=10**6+5
dp=[i for i in range(0,K)]
for i in range(0,len(dp)-1):
  dp[i+1]+=dp[i]


for i in range(T):
  l,r=case[i]
  ans=(r-l+1)*(r-2*l+1)
  if 2*l>r:
    ans=0
  else:
    if l==0:
      ans-=(dp[r-l])
    else:
      ans-=(dp[r-l]-dp[l-1])
  print(ans)
    
    
