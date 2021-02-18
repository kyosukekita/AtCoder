N=int(input())

ans=0
for i in range(1,N+1):
  ten=str(i)
  eight=oct(i)
  if ("7" not in ten) and ("7" not in eight):
    ans+=1
print(ans)  
