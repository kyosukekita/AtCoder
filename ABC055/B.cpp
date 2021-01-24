#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  int N;
  cin >> N;
  
  ll answer=1;
  rep(i,N){
    answer=answer*(i+1)%(1000000007);
  }
  
  cout << answer << endl;
}
