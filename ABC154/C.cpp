#include <bits/stdc++.h>
using namespace std;
using ll= long long;

int main() {
  int N;
  cin >> N;
  
  vector<ll> vec(N);
  for(int i=0; i<N; i++){
    cin >>vec.at(i);
  }
  
  sort(vec.begin(),vec.end());
  vec.erase(unique(vec.begin(),vec.end()), vec.end());
  
  if (vec.size()==N){
    cout << "YES" << endl;
  }else{
    cout << "NO" << endl;
  }
}
