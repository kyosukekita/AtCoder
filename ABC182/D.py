N=int(input())
A=list(map(int,input().split()))

#Aの累積和
from itertools import accumulate
b=list(accumulate(A))
c=list(accumulate(b,func=max))

ans=[0,b[0]]
now=b[0]
for i in range(1,N):
  ans.append(now+c[i])
  now+=b[i]
ans.append(now)
print(max(ans))
