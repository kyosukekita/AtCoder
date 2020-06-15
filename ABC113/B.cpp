#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  
  int T,A;
  cin >> T >> A;
  
  vector<int> H(N);
  for(int i=0; i<N; i++){
    cin >> H[i];
  }
  
  int diff=100000;
  int ans;
  
  for (int i=0; i<N; i++){
    double tmp=T-H[i]*0.006;
    if(abs(tmp-A)<diff){
      diff=abs(tmp-A);
      ans=i+1;
    }
  }
  
  cout << ans << endl;
  
  
}
