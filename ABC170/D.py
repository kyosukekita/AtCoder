N= int(input())
A=list(map(int,input().split()))

dp=[0]*(max(A)+1)

for a in A:
    for x in range(a,len(dp),a):
        dp[x]+=1

count=0
for a in A:
    if dp[a]==1:
        count+=1

print(count)



#以下は時間がかかりすぎてTLEになる解法
N= int(input())
A=list(map(int,input().split()))
 
count=0
for i in range(N):
    flag=True
    for j in range(N):
        if i!=j and A[i]%A[j]==0:
            flag=False
    if flag==True:
        count+=1
        
print(count)
