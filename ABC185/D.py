N,M= map(int, input().split())
A=list(map(int,list(input().split())))
A.sort()
A=[0]+A

white=[]
for i in range(M):
  if A[i+1]-A[i]-1!=0:
    white.append(A[i+1]-A[i]-1)
if A[-1]!=N:
  white.append(N-A[-1])

if white ==[]:
  print(0)
  exit()
  
hanko=min(white)

ans=0
for i in range(len(white)):
  if white[i]%hanko==0:
    ans+=white[i]//hanko
  else:
    ans+=white[i]//hanko+1
    
print(ans)  
  
