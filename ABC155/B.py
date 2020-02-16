N=int(input())
lis=list(map(int, input().split()))

even=[]
for i in lis:
    if i%2==0:
        even.append(i)

flag=True
for i in even:
    if i%3==0 or i%5==0:
        pass
    else:
        flag=False

if flag:
    print('APPROVED')
else:
    print('DENIED')
