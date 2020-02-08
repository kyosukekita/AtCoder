N=int(input())

def digits_sum(n):
    ds=sum([int(i) for i in list(str(n))])
    return ds
    
ans=[]    
for a in range(1,N):
    b=N-a
    ans.append(digits_sum(a)+digits_sum(b))
print(min(ans))
