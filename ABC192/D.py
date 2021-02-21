X=input()
M=int(input())

tmp=[int(i) for i in list(str(X))]
tmp=sorted(tmp, reverse=True)
d=tmp[0]

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out

if len(X)==1:#Xが1桁の場合
  if int(X) <=M:
    ans=1
  else:
    ans=0
else: #二分探索
  left=d
  right=M+1
  while right-left >1:
    mid=(left+right)//2
    if  Base_n_to_10(X,mid) >M:
      right=mid
    else:
      left=mid
  ans=left-d

print(ans)
