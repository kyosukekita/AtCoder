N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]
mod = 998244353



dp = [0] * N # dpテーブル
sdp = [0] * (N+1) # dpテーブルの累積和

# DPの初期値を設定
dp[0] = 1
sdp[1] = 1

for n in range(1, N):
    for lr in LR:
        left = max(0, n - lr[1])
        right = max(0, n - lr[0] + 1)
        dp[n] += sdp[right] - sdp[left]
        dp[n] %= mod
    sdp[n+1] = (sdp[n] + dp[n]) % mod

res = dp[N-1]
print(res)
