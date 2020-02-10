n = int(input())
a = [0]*n
b = [0]*n
c = [0]*n
for i in range(n):
    a[i],b[i],c[i] = map(int,input().split())

dpa = [a[0]]+[0]*(n-1)
dpb = [b[0]]+[0]*(n-1)
dpc = [c[0]]+[0]*(n-1)
for i in range(1,n):
    dpa[i] = max(dpb[i-1],dpc[i-1]) + a[i]
    dpb[i] = max(dpc[i-1],dpa[i-1]) + b[i]
    dpc[i] = max(dpa[i-1],dpb[i-1]) + c[i]
print(max(dpa[-1],dpb[-1],dpc[-1]))
