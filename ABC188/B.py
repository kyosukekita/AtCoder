import numpy as np
 
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
 
a=np.array(a)
b=np.array(b)
 
if(np.dot(a,b)==0):
  print("Yes")
else:
  print("No")
