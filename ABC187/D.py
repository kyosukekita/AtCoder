#https://atcoderblue.asukatagui-blog.com/abc187d/
n = int(input())
sa = []
am = 0

for i in range(n):
    a, b = map(int, input().split())
    am += a
    sa.append(2*a+b)

li = sorted(sa, reverse=True)
ans = 0

for i in range(n):
    am -= li[i]
    ans += 1
    if am < 0:
        break

print(ans)




#WA   A+B, Aでソートするのは嘘解法
N=int(input())
AB=[list(map(int,list(input().split()))) for _ in range(N)]

city=[]
for i in range(N):
  city.append([(AB[i][0]+AB[i][1]),AB[i][0]])#青木+高橋, 青木
city=sorted(city, reverse=True)

#累積和
aokitakahashi=[0 for _ in range(N+1)]
for i in range(N):
  aokitakahashi[i+1]=aokitakahashi[i]+city[i][0]
  
aoki=[0 for _ in range(N+1)]
for i in range(N):
  aoki[i+1]=aoki[i]+city[i][1]

for i in range(1,N+1):
  if (aokitakahashi[i])>(aoki[N]-aoki[i]):
    print(i)
    break
    
print(city)
print(aokitakahashi)
print(aoki)
