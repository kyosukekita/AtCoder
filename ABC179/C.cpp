#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
  ll N;
  cin >> N;
  ll ans =0;
  for(int i=1; i<N;i++){
    if(N%i==0){
      ans+= ll(N/i)-1;
    }else{
      ans+=ll(N/i);
    }
  }
  cout << ans << endl;
}
