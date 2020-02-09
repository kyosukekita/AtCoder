#累積和　　適切な前処理をしておくことで、配列上の区間の総和を求めるクエリを爆速で処理できるようになる.

from itertools import accumulate

N,K = map(int, input().split())
p=list(map(int,input().split()))

q=[0]+p
q=list(accumulate(q)) 

ans=[]
for i in range(N-K+1):
    ans.append(((q[i+K]-q[i])+K)*0.5)

print(max(ans))
