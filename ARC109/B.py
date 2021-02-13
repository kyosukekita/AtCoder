N=int(input())
#N+1を1,2,3,,,に分割すればよいので、1+2+3+...x<=N+1
#を満たす最大のxを求めると、N+1-xが答えとなる
#二分探索

left=0
right=2*10**9
while right-left>1:
  mid=(left+right)//2
  if mid*(mid+1)//2 <=N+1:
    left=mid
  else:
    right=mid

print(N+1-left)
