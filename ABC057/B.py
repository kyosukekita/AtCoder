N,M=map(int,input().split())

student=[]
point=[]

for i in range(N):
  student.append(list(map(int,input().split())))

for i in range(M):
  point.append(list(map(int,input().split())))


for i in range(N):
  distance=float("inf")
  id=0
  for j in range(M):
    if abs(student[i][0]-point[j][0])+abs(student[i][1]-point[j][1]) < distance:
      distance= abs(student[i][0]-point[j][0])+abs(student[i][1]-point[j][1])
      id=j+1
  
  print(id)
