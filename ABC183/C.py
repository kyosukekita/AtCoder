N,K=map(int, input().split())
T=[list(map(int,list(input().split()))) for _ in range(N)]

ans=0
import itertools
tmp=[i for i in range(2,N+1)]
for keiro in itertools.permutations(tmp):#2=Nまでの順列生成
  goukei=0
  goukei+=T[0][keiro[0]-1]#都市1から～
  for i in range(len(keiro)-1):
    goukei+=T[keiro[i]-1][keiro[i+1]-1]
  goukei+=T[keiro[-1]-1][0]#最後に都市1に帰ってくる
  
  if goukei==K:
    ans+=1
    
print(ans)  
