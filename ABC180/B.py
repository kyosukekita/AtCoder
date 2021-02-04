import math
import sys
sys.setrecursionlimit(10**6)

N=int(input())
x=list(map(int, input().split()))

man=0
for i in range(N):
  man+=abs(x[i])
print(man)

eu=0
for i in range(N):
  eu+=pow(x[i],2)
print(math.sqrt(eu))

print(max([abs(i) for i in x]))
