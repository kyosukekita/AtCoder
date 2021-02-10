



#一部TLEを起こす
S=input()
candidates=[str(i*2019) for i in range(1,101)]

import re

ans=0
for i in range(len(S)):#2*10**5
  for candidate in candidates:#100
    if S[i:].startswith(candidate):
      ans+=1
print(ans)
