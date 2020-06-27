#Xの約数の個数はO(X**0.5)時間で求められるが、X=1,2,...10**7の全てでこれを行う時間はない
n=int(input())

answer=0
for x in range(1,n+1):
  y=n//x
  answer+=y*(y+1)*x/2
print(int(answer))
