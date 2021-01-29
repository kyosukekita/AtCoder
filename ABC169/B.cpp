#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

int main() {
  int N;
  cin >> N;
  
  vector<ll> A(N); 
  for(int i=0; i<N; i++){
    cin >> A[i];
  }
  
  for(int i=0; i<N; i++){
    if(A[i]==0){
      cout << 0 << endl;
      return 0;
    }
  }
  
  ll ans=1;
  for(int i=0;i<N;i++){
    //C++多倍長の問題に注意
    if(A[i]<=1000000000000000000/ans){
      ans*=A[i];
    }else{
      cout << -1 << endl;
      return 0;
    }
  }
  cout << ans << endl;
}
