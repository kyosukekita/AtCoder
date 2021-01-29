#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

vector<pair<ll,ll>> prime_factorize(ll n){
  vector<pair<ll, ll>> res;
  for(ll p=2; p*p<=n; p++){
    if(n%p !=0) continue;
    ll num=0;//指数部分
    while (n%p==0){
      num++;
      n/=p;
    }
    res.push_back(make_pair(p,num));
  }
  if(n!=1) res.push_back(make_pair(n,1));
  return res;
}


int main() {
  ll n;
  cin >> n;
  
  auto pf=prime_factorize(n);
  ll res=0;
  for(auto p: pf){
    ll e=p.second;
    ll tmp=0, cur=1;
    while(e>=cur) e-=cur++, tmp++;
    res +=tmp;
  }
  cout << res << endl;
}
  
