N=int(input())

MODE=10**9+7

answer=1
for i in range(1,N+1):
  answer=(answer*i)%MODE

print(answer)
