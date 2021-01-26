#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  ll N,M;
  cin >> N>> M;
  
  vector<pair<ll,ll>> city(M);
  vector<vector<ll>> cnt(N+1);
  rep(i,M){
    ll P,Y;
    cin >> P >> Y;
    city.at(i)=make_pair(P,Y);
    cnt[P].push_back(Y);
  }
  rep(i,N+1){
    sort(cnt[i].begin(), cnt[i].end());
  }
  
  rep(i,M){
    ll p,y;
    p=city[i].first;
    y=city[i].second;
    ll d=distance(cnt[p].begin(), lower_bound(cnt[p].begin(), cnt[p].end(),y))+1;
    printf("%06lld%06lld\n",p,d);
  }
}
