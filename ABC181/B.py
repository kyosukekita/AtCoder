N= int(input())
A=[]
 
for i in range(N):
    A.append(list(map(int, input().split())))
 
 
count=0
for i in range(N):
  count+=(1+A[i][1])*(A[i][1])/2-(A[i][-0])*(A[i][0]-1)/2
             
print(int(count))
