K=int(input())

A=[0 for _ in range(10**7)] #A[i]=0(mod K)となる最小のiを求めよ
A[0]=7%K
for i in range(1,K+1):
  A[i]=(A[i-1]*10+7)%K

for i in range(K+1):
  if A[i]==0:
    print(i+1)
    exit()
    
print(-1)



def calc(k):
    cur = 0
    for i in range(1, 10 ** 7):
        cur *= 10
        cur += 7
        cur %= k
        if cur == 0:
            return i

    return -1


k = int(input())
print(calc(k))
