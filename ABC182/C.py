import itertools

N=input()
k=len(N)

keta=[i for i in range(k)]

for i in range(k):
  for tmp in itertools.combinations(keta,k-i):
    tmp_list=list(tmp)
    goukei=0
    for j in tmp_list:
      goukei+=int(N[j])
    
    if goukei%3==0:
      print(i)
      exit()
      
print(-1)
