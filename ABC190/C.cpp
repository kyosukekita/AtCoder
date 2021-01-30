#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

int main() {
  int N,M; 
  cin >> N >> M;
  
  vector<pair<int,int>> condition(M);
  int A,B;
  for(int i=0; i<M;i++){
    cin >> A >> B;
    condition[i]=make_pair(A,B);
  }
  
  int K;
  cin >> K;
  
  vector<pair<int,int>> plate(K);
  for(int i=0; i<K;i++){
    cin >> A >> B;
    plate[i]=make_pair(A,B);
  }
  
  ll ans=0;
  for(ll bit=0; bit<(1<<K); bit++){
    vector<bool> ball(N);
    for(int i=0; i<K; i++){
      const auto [C,D] = plate[i];
      if(bit & 1<<i){
        ball[C]=1;
      }else{
        ball[D]=1;
      }
    }
    ll cnt=0;
    for(auto [A,B]: condition){
      if(ball[A] && ball[B]){
        cnt++;
      }
    }
    
    if (ans<cnt){
      ans=cnt;
    }
  }
      
    
  cout << ans << endl;
 
}
