"""N個の足場があります足場には 1,2,3...Nと番号が振られています.各i(1<i<N)について、足場iの高さはhです。
最初、足場1にカエルがいます。カエルは次の行動を何回か繰り返し、足場Nまでたどり着こうとしています。
足場iにいるとき、足場 i+1または i+2へジャンプする。 このとき、ジャンプ先の足場を jとすると、コスト |hi−hj|
を支払う。カエルが足場 N に辿り着くまでに支払うコストの総和の最小値を求めてください。"""

#iにたどり着くまでの最小スコアを考える。dp[i]はカエルが足場iへと移動するのに必要な最小コスト

N=int(input())
h=list(map(int,input().split()))

dp=[0]*(N)

for i in range(1,N):
    if i==1:
        dp[i]=abs(h[i]-h[i-1])
    else:
        dp[i]=min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i]-h[i-2]))

print(dp[N-1])
