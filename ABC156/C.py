N=int(input())
X=list(map(int,input().split()))

#P=int(sum(X)/N)


temp=[]
for p  in range(0,3*N): #この解法は正当ではない。3*Nにしたら偶然うまくいった。
    answer=0
    for i in X:
        answer+=((i-p)**2)
    temp.append(answer)

print(min(temp))
