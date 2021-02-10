import itertools

#入力
N,M,Q = map(int, input().split())
s=[list(map(int,list(input().split()))) for _ in range(Q)]

#得点を計算する関数
def point(s,A):
  ans=0
  for i in range(len(s)):
    if A[s[i][1]-1]-A[s[i][0]-1]==s[i][2]:
      ans+=s[i][3]
  return ans
  
max_point=0
tmp=[i for i in range(1,M+1)]
for i in itertools.combinations_with_replacement(tmp,N):
  A=list(i)
  max_point=max(max_point, point(s,A))
print(max_point)
  
