#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int intToBit(int n){
  bitset<10> bit;//10桁用意する
  while(n>0){
    bit.set(n%10);//桁の番号の場所に1を立てる
    n/=10;
  }
  return bit.to_ullong();
}


int main(){
  int N,K;
  cin >> N >> K;
  vector<int> D(K);
  rep(i,K){
    cin>> D.at(i);
  }
  
  bitset<10> hate;
  rep(i,K){
    hate.set(D.at(i));
  }
  int hate1;
  hate1=hate.to_ullong();
  
  int res=N;
  while (true){
    if (!(intToBit(res)& hate1)){
      break;
    }
    res++;
  }
  cout << res << endl;
}
