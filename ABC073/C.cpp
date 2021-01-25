#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  ll N;
  cin >> N;
  
  map<ll,ll> A;
  ll number;
  rep(i,N){
    cin >> number;
    
    if(A.count(number)){
      A[number]+=1;
    }else{
      A[number]=1;
    }
  }
  
  ll count=0;
  for(auto iter=A.begin(); iter!=A.end();iter++){
    if((iter->second)%2!=0){
      count++;
    }
  }
  cout << count << endl;
}
