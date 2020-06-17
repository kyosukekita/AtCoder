//https://atcoder.jp/contests/abc081/submissions/14160409
#include <bits/stdc++.h>
using namespace std;

  
int main() {
  int N,K;
  cin >> N >>K;
  
  vector<int> A(N);  
  for(int i=0; i<N; i++){
    cin >> A[i];
  }
  
  vector<int> bucket(200001,0);
  for(int i=0; i<N;i++){
    bucket.at(A.at(i))++;
  }
  
  if (bucket.size() <=K){
    cout << 0 << endl;
    return 0;
  }else{
    sort(bucket.begin(), bucket.end());
    int ball = bucket.size()-K;
    int count=0;
    for(int i=0; i<ball; i++){
      count+=bucket.at(i);
    }
    cout << count << endl;
    return 0;
  }
}
