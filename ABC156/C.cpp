#include <bits/stdc++.h>
using namespace std;
using ll= long long ;
#define INF 10000000000;
 
int main() {
  int N;
  cin >>N;
  
  vector<int> X(N);
  for(int i=0; i<N; i++){
    cin >> X.at(i);
  }
  sort(X.begin(), X.end());
  
  ll sum=INF;
  for (int j=X[0]; j<=X[N-1]; j++){
    ll tmp=0;
    for(int i=0; i<N; i++){
      tmp+=(X[i]-j)*(X[i]-j);
      
    }
    if(tmp<sum){
      sum=tmp;
    }
  }
  cout << sum << endl;
}
