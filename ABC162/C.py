#3重ループにするとTLEなので工夫しました。

K=int(input())
import math

tmp=[]
for a in range(1,K+1):
  tmp1=[]
  for b in range(1,K+1):
    tmp1.append(math.gcd(a,b))
  tmp+=tmp1
  
  
ans=0
for i in range(len(tmp)):
  for c in range(1,K+1):
      ans+=math.gcd(tmp[i],c)
print(ans)
