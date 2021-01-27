#include <bits/stdc++.h>
using namespace std;
using ll= long long;

int main() {
  ll H;
  cin >> H;
  
  ll cnt=0;
  while(H>0){
    H/=2;
    cnt++;
  }
  
  ll ans=0;
  for(int i=0;i<cnt;i++){
    ans+=pow(2,i);
  }
  
  cout << ans << endl;
}
