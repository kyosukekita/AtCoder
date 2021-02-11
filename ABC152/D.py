ans=0
N=int(input())

d={}# "01","02", ... "98", "99"
for i in range(1,100):
  if len(str(i))==1:
    d["0"+str(i)]=0
  else:
    d[str(i)]=0

for i in range(1,N+1):#もしもiが205ならば
  number = str(i)[0] + str(i)[-1] # "2"+"5" ="25"
  d[number]+=1

d_keys=list(d.keys())
ans=0

for key in d_keys:
  ans+=d[key]*d[key[::-1]] d["25"]の数とd["52"]の組み合わせ
print(ans)  
