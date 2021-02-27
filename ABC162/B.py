N=int(input())
tmp=[0 for _ in range(N+2)]
for i in range(1,N+2):
  if i%3!=0 and i%5!=0:
    tmp[i]=i
    
print(sum(tmp[:N+1]))
