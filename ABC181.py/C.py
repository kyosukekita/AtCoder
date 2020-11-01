N= int(input())
A=[]
for i in range(N):
    A.append(list(map(int, input().split())))

flag=False
for i in range(N):
    B0=[]
    B1=[]
    for j in range(N):
        if i!=j:
            B0.append(A[j][0]-A[i][0])
            B1.append(A[j][1]-A[i][1])
    if B0.count(0)>=2 or B1.count(0)>=2:
        print("Yes")
        flag=True
        break
           
    for x in range(N-1):
        for y in range(N-1):
            if x!=y and B0[x]!=0 and B1[y]!=0 and B0[y]!=0 and B1[x]!=0 :
                if(B0[x]*B1[y]==B0[y]*B1[x]):
                  print("Yes")
                  flag=True
                  break
        
        if flag:
          break
    if flag:
      break          
            
            
if flag==False:
    print("No")
