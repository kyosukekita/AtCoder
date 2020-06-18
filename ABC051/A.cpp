#include <bits/stdc++.h>
using namespace std;

  
int main() {
  string s;
  cin >> s;
  
  s.replace(5,1," ");//str.replace(開始位置,長さ,文字列)
  s.replace(13,1," ");
  //単純にs[5],s[13]だけで良い。
  cout << s  << endl;
}
