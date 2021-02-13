import math #結局pythonで平方根とるにはmath.sqrt()が一番いいらしい

n=int(input())

xy=[]
for i in range(n):
  x,y=map(int,input().split())
  xy.append([x,y])


max_length=0
for i in range(n):
  for j in range(i+1,n):
    l=math.sqrt((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)
    max_length=max(max_length,l)

print(max_length)
