N, K = map(int, input().split())
H=list(map(int,input().split()))
H=sorted(H, reverse=True)

ans=sum(H)
for i in range(K):
    if N>=K:
        ans -=H[i]
    else:
        ans=0

print(ans)
