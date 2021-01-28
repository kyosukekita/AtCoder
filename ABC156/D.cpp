//https://atcoder.jp/contests/abc156/submissions/19702320
int modcmb(int n, int r, int mod){
  int x=1;
  int y=1;
  for(int i=0; i<r;i++){
    x=x*(n-i)%mod;
    y=y*(i+1)%mod;
  }
  return x*modpow(y,mod-2,mod)%mod;
}








//REになってしまう解法
#include <bits/stdc++.h>
using namespace std;
using ll= long long ;
 
long long comb(int n, int r){
  vector<vector<long long>> v(n+1, vector<long long>(n+1,0));
  for(int i=0; i< v.size(); i++){
    v[i][0]=1;
    v[i][i]=1;
  }
  for(int j=1; j<v.size(); j++){
    for(int k=1; k<j; k++){
      v[j][k]=(v[j-1][k-1]+v[j-1][k]);
    }
  }
  return v[n][r];
}
 
int main() {
  int n,a,b;
  cin >> n >> a >> b;
  ll mod = 100000007;
  ll answer=pow(2,n)-comb(n,a)-comb(n,b)-1;
  cout << answer%mod << endl;
}


#include <bits/stdc++.h>
using namespace std;

template<int MOD> struct Fp {
    long long val;
    constexpr Fp(long long v = 0) noexcept : val(v % MOD) {
        if (val < 0) val += MOD;
    }
    constexpr int getmod() { return MOD; }
    constexpr Fp operator - () const noexcept {
        return val ? MOD - val : 0;
    }
    constexpr Fp operator + (const Fp& r) const noexcept { return Fp(*this) += r; }
    constexpr Fp operator - (const Fp& r) const noexcept { return Fp(*this) -= r; }
    constexpr Fp operator * (const Fp& r) const noexcept { return Fp(*this) *= r; }
    constexpr Fp operator / (const Fp& r) const noexcept { return Fp(*this) /= r; }
    constexpr Fp& operator += (const Fp& r) noexcept {
        val += r.val;
        if (val >= MOD) val -= MOD;
        return *this;
    }
    constexpr Fp& operator -= (const Fp& r) noexcept {
        val -= r.val;
        if (val < 0) val += MOD;
        return *this;
    }
    constexpr Fp& operator *= (const Fp& r) noexcept {
        val = val * r.val % MOD;
        return *this;
    }
    constexpr Fp& operator /= (const Fp& r) noexcept {
        long long a = r.val, b = MOD, u = 1, v = 0;
        while (b) {
            long long t = a / b;
            a -= t * b; swap(a, b);
            u -= t * v; swap(u, v);
        }
        val = val * u % MOD;
        if (val < 0) val += MOD;
        return *this;
    }
    constexpr bool operator == (const Fp& r) const noexcept {
        return this->val == r.val;
    }
    constexpr bool operator != (const Fp& r) const noexcept {
        return this->val != r.val;
    }
    friend constexpr ostream& operator << (ostream &os, const Fp<MOD>& x) noexcept {
        return os << x.val;
    }
    friend constexpr Fp<MOD> modpow(const Fp<MOD> &a, long long n) noexcept {
        if (n == 0) return 1;
        auto t = modpow(a, n / 2);
        t = t * t;
        if (n & 1) t = t * a;
        return t;
    }
};

const int MOD = 1000000007;
using mint = Fp<MOD>;

mint calc(long long N, long long K) {
    mint res = 1;
    for (long long n = 0; n < K; ++n) {
        res *= (N - n);
        res /= (n + 1);
    }
    return res;
}

int main() {
    long long N, A, B;
    cin >> N >> A >> B;
    mint res = modpow(mint(2), N) - 1;
    res -= calc(N, A) + calc(N, B);
    cout << res << endl;
}
