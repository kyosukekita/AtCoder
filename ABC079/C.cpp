#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<(n); i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  string s;
  cin >> s;
  vector<int> d(4);
  rep(i, 4) d[i] = s[i] - '0';
  int sum = 0;
  rep(bit, 1 << 3){
    sum = d[0];
    rep(i, 3){
      if ((bit & (1 << i)) != 0){
        sum += d[i + 1];
      } else {
        sum -= d[i + 1];
      }
    }
    if (sum == 7){
      cout << d[0];
      rep(j, 3){
        if ((bit & (1 << j)) != 0){
          cout << '+';
        } else {
          cout << '-';
        }
        cout << d[j + 1];
      }
      cout << "=7" << endl;
      return 0;
    }
  }
  return 0;
}
