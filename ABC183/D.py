#典型的なimos法
N,W=map(int, input().split())
STP=[list(map(int,list(input().split()))) for _ in range(N)]

import itertools

time=[0 for _ in range(2*(10**5)+3)]
for i in range(N):
  time[STP[i][0]]+=STP[i][2]
  time[STP[i][1]]-=STP[i][2]#添え字に注意。最後のＴiは含まない
    
time_accume=list(itertools.accumulate(time))

if max(time_accume)>W:
  print("No")
else:
  print("Yes")
