n=int(input())

mod=1000000007

power=1
for i in range(1,n+1):
  power=(power*i)%mod
print(power)
