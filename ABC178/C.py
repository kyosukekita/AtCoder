n=int(input())
mod=10**9+7

ten=1
for _ in range(n):
  ten=(ten*10)%mod

nine=1
for _ in range(n):
  nine=(nine*9)%mod
  
eight=1
for _ in range(n):
  eight=(eight*8)%mod
  
ans=ten+eight-nine-nine
print(ans%mod) #pythonでは負のmodも計算してくれるから楽だよね
