n=int(input())
A=list(map(int,input().split()))
A.sort()
answer=1

for i in range(n):
  answer*=A[i]
  if(answer>10**18):
    print(-1)
    exit()
    
print(answer)
