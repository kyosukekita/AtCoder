//https://atcoder.jp/contests/abc042/submissions/13187994

#include "bits/stdc++.h"
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
 
int intToBit(int num){
  int bit=0;
  while(1){
    int tmp;
    tmp = num%10;
    bit |= (1<<tmp);//ビットbitにi番目のフラグを立てる
    num /= 10;
    if(num == 0) break;
  }
  return bit;
}
 
int main() {
  int N,K;
  cin >> N >> K;
  int hate=0;
  rep(i,K){
    int D;
    cin >> D;
    hate |= (1<<D);
  }
  int res = N;
  while(1){
    if(!(intToBit(res) & hate)) break;//intToBit(res)とhateのフラグの立っている位置が同じでない。
    res++;
  }
  cout << res << endl;
  return 0;
}
