#TLEになる
N=int(input())
S=input()

count=0
for i in range(N+1):
  for j in range(1,N+1):
    if i+j+j<N:
      if (S[i]!=S[i+j] and S[i+j]!=S[i+j+j] and S[i]!=S[i+j+j]):
      	count+=1

print(S.count("R")*S.count("G")*S.count("B")-count)
