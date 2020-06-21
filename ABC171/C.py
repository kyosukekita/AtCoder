n=int(input())

lis=[26, 702, 18278, 475254, 12356630, 321272406, 8353082582, 217180147158, 5646683826134, 146813779479510, 1000000000000001]


k=0#答えが何桁になるか調べる
for i in range(len(lis)):
  if lis[i]>=n:
    k=i
    break

s=""
if k==0:
  s+=chr(n+96)
else:
  for i in range(k+1):
    n-=1
    x=int(n%26)
    s+=(chr(x+ord('a')))
    n=int(n//26)

print(s[::-1])
