#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

int main(){
  int N, X;
  cin >> N >> X;
  
  vector<ll> vec(N);
  for(int i=0; i<N; i++){
    ll v,p;
    cin >> v >> p;
    vec[i]=v*p;
  }
  
  int alco=0;
  int ans=-1;
  for(int i=0; i<N;i++){
    alco+=vec[i];
    if(alco>X*100){
      ans=i+1;
      break;
    }
  }
  cout << ans << endl;
}
