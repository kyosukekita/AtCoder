N=int(input())
S = [input() for _ in range(N)]

from collections import defaultdict
tmp=defaultdict(int)

for i in range(N):
  if S[i][0]=="!":#先頭に!がついていたら、
    if S[i][1:] in tmp:
      print(S[i][1:])
      exit()
    
    tmp[S[i]]+=1
 
  else:#先頭に!がついていなかったら、
    if ("!"+S[i]) in tmp:
      print(S[i])
      exit()
    tmp[S[i]]+=1

print("satisfiable")
