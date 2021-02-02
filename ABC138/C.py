N= int(input())
v=list(map(int,input().split()))

while (len(v)!=1):
  v.sort()
  maxi=v.pop(0)
  mini=v.pop(0)
  v.append((mini+maxi)/2)
  

print(v[0])
