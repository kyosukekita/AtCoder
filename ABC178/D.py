S=int(input())
mod=10**9+7

dp=[0 for _ in range(S+1)]#dp[i]: 総和がiとなるときの場合の数の和
dp[0]=1

for i in range(S+1):
  for d in range((i-3)+1):
    dp[i]+=dp[d]%mod

print(dp[S]%mod)



#高速化https://drken1215.hatenablog.com/entry/2020/10/11/211000 
S=int(input())
mod=10**9+7

dp=[0 for _ in range(2002)]
dp[0]=1
dp[1]=dp[2]=0 #総和がiとなるときの

for i in range(3,S+1):
  dp[i]=(dp[i-1]+dp[i-3])%mod
      
print(dp[S])
