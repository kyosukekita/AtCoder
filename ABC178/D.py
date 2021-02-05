S=int(input())
mod=10**9+7

dp=[0 for _ in range(2002)]
dp[0]=1
dp[1]=dp[2]=0 #総和がiとなるときの

for i in range(3,S+1):
  dp[i]=(dp[i-1]+dp[i-3])%mod
      
print(dp[S])
