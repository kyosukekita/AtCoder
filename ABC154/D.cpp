#include <bits/stdc++.h>
using namespace std;
 
int main() {
  //入力
  int N,K; cin >> N >> K;
  
  vector<int> p(N);
  for(int i=0; i<N; i++){
    cin >> p.at(i);
  }
  
  //累積和を計算
  vector<int> s(N+1,0);
  for(int i=0; i<N; i++) s[i+1]=s[i]+(1+p[i]);//int型を保つためにここで÷2してはいけない
  //答えを求める
  double res=0;
  for(int i=0;i<N-K+1;i++){
    int val =(s[K+i]-s[i]);
    if(res<val) res=val;
  }
  
  cout << fixed<<setprecision(10)<< res/2 << endl;
}
