N,K = map(int, input().split())

answer=0
while N>0:
    N=int(N/K)
    answer+=1

print(answer)
