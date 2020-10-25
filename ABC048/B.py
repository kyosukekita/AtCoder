a,b,x= map(int, input().split())

a=(a-1)//x #1~a-1までにxで割り切れるものがいくつ出現するか
b=b//x #1~bまでにxで割り切れるものがいくつ出現するか
print(b-a)
