








#正解は出るが一部TLEになってしまう実装
N=int(input())
A=list(map(int,input().split()))
 
count=1
 
j=0
for i in range(N+1):
  k=i
  if (A[j:k]==sorted(A[j:k]) or A[j:k]==sorted(A[j:k],reverse=True)):
    continue
  else:
    count+=1
    j=i-1
    
print(count)
