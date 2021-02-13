a,b,x,y=map(int, input().split())

t=abs(a-b)

if t==0:
  print(x)
  exit()
  
if x*2<y:
  if b<a:
    print(2*x*(t-1)+x)
  else:
    print(2*x*t+x)
else:
  if b<a:
    print(min(y*t+x, y*(t-1)+x))
  else:
    print(y*t+x)
