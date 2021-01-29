#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

string intTostring(int n){
  string s;
  s= (n + 97-1);//今回は96から
  return s;
}

int main(){
  ll N; cin >> N;
  string ans;
  while(N>0){
    if(N%26==0){
      ans=intTostring(26)+ans;
      N/=26;
      N--;
    }else{
      ans=intTostring(N%26)+ans;
      N/=26;
    }
    
  }
  cout << ans << endl;
}  
