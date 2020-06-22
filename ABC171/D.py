#https://atcoder.jp/contests/abc171/submissions/14600431
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())
s = sum(a)
a = Counter(a)
for _ in range(q):
    b, c = map(int, input().split())
    if b in a:
        a[c] += a[b]
        s += (c-b) * a[b]
        a[b] = 0
    print(s)



#愚直にやってＴＬＥをくらった解法
n=int(input())
A=list(map(int, input().split()))
 
q=int(input())
BC=[list(map(int,list(input().split()))) for _ in range(q)]
 
for i in range(q):
  for j in range(n):
    if A[j]==BC[i][0]:
      A[j]=BC[i][1]
  print(sum(A))
