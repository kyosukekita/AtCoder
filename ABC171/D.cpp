//https://drken1215.hatenablog.com/entry/2020/06/21/224900
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Q;
    cin >> N;
    long long sum = 0;
    vector<long long> num(110000, 0);//バケットに変換 num[b]はbが現れる回数
    for (int i = 0; i < N; ++i) {
        long long A; cin >> A;
        sum += A;
        num[A]++;
    }
        
    cin >> Q;
    for (int i = 0; i < Q; ++i) {
        long long B, C; cin >> B >> C;
        sum += (C - B) * num[B];
        num[C] += num[B];
        num[B] = 0;
        cout << sum << endl;
     }
}




//TLEを食らう解法
#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

int main(){
  int N; cin >> N;
  vector<int> A(N);
  for(int i=0; i<N; i++){
    cin >> A[i];
  }
  
  int Q; cin >> Q;
  vector<int> B(Q);
  vector<int> C(Q);
  
  for(int i=0; i<Q;i++){
    cin >> B[i] >> C[i];
  }
  
  ll sum=accumulate(A.begin(), A.end(),0);
  
  vector<int> cnt(Q);
  for(int i=0; i<Q; i++){
    int cnt=0;
    cnt=count(A.begin(), A.end(), B[i]);
    sum+=cnt*(C[i]-B[i]);
    cout << sum << endl;
    replace(A.begin(), A.end(),B[i],C[i]);
  }
}  
