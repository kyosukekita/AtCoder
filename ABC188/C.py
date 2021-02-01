n=int(input())
a=list(map(int,input().split()))

first=a[:pow(2,n-1)]
second=a[pow(2,n-1):]

if(max(first)<max(second)):
  print(a.index(max(first))+1)
else:
  print(a.index(max(second))+1)
