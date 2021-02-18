N=int(input())
A=list(map(int,list(input().split())))
A.sort()#Aの並びを変えても答えはかわらない

import itertools
tmp=list(itertools.accumulate(A))

ans=0
for i in range(N):
  ans+=A[i]*(i+1)-tmp[i]
  

print(ans)
