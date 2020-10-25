N,x= map(int, input().split())
A=list(map(int,input().split()))

count=0
for i in range(0,N-1):
  if A[0]>x:
    count+=(A[0]-x)
    A[0]=x
    
  if A[i]+A[i+1]-x>0:
    count+=(A[i+1]+A[i]-x)
    A[i+1]=(x-A[i])
    

print(count)
