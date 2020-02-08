N=int(input())
Y=int(input())

res10000=-1
res5000=-1
res1000=-1

for i in range(N+1):
    for j in range(N-i+1):
        k=N-i-j
        if (10000*i+5000*j+1000*k)==Y:
            res10000=i
            res5000=j
            res1000=k
print(res10000,res5000,res1000)
