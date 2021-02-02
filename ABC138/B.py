N= int(input())
A=list(map(int,input().split()))


if N==1:
  print(A[0])
else:
  bunshi=1
  for i in range(N):
    bunshi*=A[i]
    
  bunbo=sum([bunshi/a for a in A])

  print(bunshi/bunbo)
  

#模範解答
N= int(input())
A = map(int, input().split())
print('{:.16g}'.format(1 / sum(1 / x for x in A)))
