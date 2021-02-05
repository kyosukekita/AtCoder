N=int(input())
A=list(map(int,input().split()))
mod=10**9+7

#累積和
B=[0 for _ in range(N+1)]
for i in range(N):
  B[i+1]=B[i]+A[i]

ans=0
for i in range(N-1):
    ans+=(A[i]*(B[N]-B[i+1]))%mod
    
print(ans%mod)
