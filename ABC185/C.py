#itertools使わなくてもよい。
＃重複組み合わせ
#L個の〇と11本の仕切りを並べる重複組み合わせ
#n 種類のものから重複を許して r 個選ぶ場合の数はnHr=n+r−1Cr 通り
#(L-11)+11-1C11

L=int(input())
from math import comb
ans = comb(L-1, 11)
print(ans)
