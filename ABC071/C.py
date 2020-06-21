#AtCoderをpythonでするときはライブラリを使った方がいい。Counterrもその一つ

import collections
n = int(input())
a_lst = list(map(int, input().split()))
 
c = collections.Counter(a_lst)
cand = [k for k, v in c.items() if v >= 2]
cand = sorted(cand)
 
if len(cand) >= 2:
  if c[cand[-1]] >= 4:
    print(cand[-1] ** 2)
  else:
    print(cand[-2] * cand[-1])
else:
  print(0)
