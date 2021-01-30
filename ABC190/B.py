N,S,D = map(int, input().split())

magic = []
for i in range(N):
  x,y = map(int, input().split())
  magic.append([x,y])

flag=False

for i in range(N):
  if (magic[i][0] <S) & (magic[i][1]>D):
    flag=True
    break
    
if (flag):
  print("Yes")
else:
  print("No")
  
