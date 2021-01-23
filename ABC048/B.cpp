#include <bits/stdc++.h>
using namespace std;


int main() {
  long long a,b,x;
  cin >> a>> b>> x;
  
  if (a==0){
    cout << b/x+1;//C++では、整数型を項とする演算子の結果は代表的な章から小数部を切り捨てたものとなる。
  }else{
    cout<< (b/x)-(a-1)/x;
  }
}
