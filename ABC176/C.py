N = int(input())
A=list(map(int,input().split()))

ans=0
highest=A[0]
for i in range(1,N):
  if A[i]<highest:
    ans+=highest-A[i]
  else:
    highest=A[i]
print(ans)  
