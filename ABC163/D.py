N,K=map(int,input().split())
mod=10**9+7

#0~Nの中からK個選んだ時に考えられる合計値の総数
#合計が同じでも、個数が異なれば別の個数としてカウント
tmp=[i for i in range(0,N+1)]
import itertools
ruiseki=list(itertools.accumulate(tmp))

ans=0
for i in range(K,N+1):
  ans+=((ruiseki[-1]-ruiseki[-i-1])-ruiseki[i-1]+1)%mod

print((ans+1)%mod)
