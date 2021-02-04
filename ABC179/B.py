N=int(input())
D=[list(map(int, input().split())) for _ in range(N)]

ans=False
for i in range(N-2):
  if len(set(D[i]))==len(set(D[i+1]))==len(set(D[i+2]))==1:
    ans=True
    break

if (ans):
  print("Yes")
else:
  print("No")
