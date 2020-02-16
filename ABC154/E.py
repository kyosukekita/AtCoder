#桁DP (https://qiita.com/takayg1/items/a5c1cadbc8b89daa0fd5)

"""1以上N以下の整数であって、10 進法で表したときに、
0 でない数字がちょうど K 個あるようなものの個数を求めてください。"""

"""dp[i][j][k]:i桁目までを決めて、Ｎ未満で確定ならj=1, Nと一致しているならばj=0、
そのとき0でない数をk個含む"""


N = input()
K = int(input())
m = len(N)
dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(m + 1)]
dp[0][0][0] = 1

for i in range(1, m + 1):
    l = int(N[i - 1])
    for k in range(K + 1):
        dp[i][1][k] += dp[i - 1][1][k]
        if l != 0:
            dp[i][1][k] += dp[i - 1][0][k]
        else:
            dp[i][0][k] += dp[i - 1][0][k]
        if k - 1 >= 0:
            dp[i][1][k] += 9 * dp[i - 1][1][k - 1]
            if l != 0:
                dp[i][0][k] += dp[i - 1][0][k - 1]
                dp[i][1][k] += (l - 1) * dp[i - 1][0][k - 1]

print(dp[m][0][K] + dp[m][1][K])

#以下TLE
N=int(input())
K=int(input())

def CountNotZero(n):
    NotZero=0
    while n>0:
        if (n%10)!=0:
            NotZero+=1
        n=int(n/10)  
    return NotZero

def main(n,k):
    answer=0
    while n>0: 
        if CountNotZero(n)==k:
            answer+=1
        n-=1
    return answer

print(main(N,K))
