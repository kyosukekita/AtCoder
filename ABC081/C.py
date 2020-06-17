N,K=map(int,input().split())
A = list(map(int, input().split()))

count={}

for i in range(N):
  if A[i] not in count:
    count[A[i]]=1
  else:
    count[A[i]]+=1

if(len(count)<=K):
  print(0)
else:
  x=len(count)-K #減らさなければならない種類
  answer=0
  sorted_count=sorted(count.items(),key=lambda x:x[1])
  for i in range(x):
    answer+=int(sorted_count[i][1])
  
  print(answer)
