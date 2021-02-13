#問題文よく見て
N,M=map(int, input().split())
p=[]
S=[]
for i in range(M):
  pi,Si =input().split()
  p.append(int(pi))
  S.append(Si)
  
AC=[0 for _ in range(N)]
WA=[0 for _ in range(N)]

for i  in range(M):
  if S[i]=="AC":
    if AC[p[i]-1]==0:
      AC[p[i]-1]=1
  elif S[i]=="WA":
    if AC[p[i]-1]==0:
      WA[p[i]-1]+=1

for i in range(N):
  if AC[i]==0:
    WA[i]=0
    
print(sum(AC), sum(WA))
