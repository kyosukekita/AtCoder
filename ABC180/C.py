N=int(input())

import math
#nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  table = []
  tmp=int(math.sqrt(n))
  for i in range(1, tmp+1):
    if n%i==0:
      table.append(i)
      table.append(int(n/i))
  table=list(set(table))
  table.sort()
  return table

ans=prime_decomposition(N)
for i in ans:
  print(i)
