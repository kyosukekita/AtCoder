N=int(input())

keihin={} #これをリストにするといけない。N個の単語について、最悪N回探索をするのでN^2時間になる
for i in range(N):
  S=input()
  if S not in keihin:
    keihin[S]=1
    
print(len(keihin))
