X,Y = map(int, input().split())

flag=False

for x in range(0,X+1):
    if (2*x+4*(X-x))==Y:
        flag=True
        break

if flag:
    print("Yes")
else:
    print("No")
