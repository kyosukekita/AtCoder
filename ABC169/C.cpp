#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

int main() {
  ll A;
  double B;
  cin >> A >> B;
  
  ll c= B*100+0.001;
  cout<< A*c/100 << endl;
}


//文字列として扱うのも確実
#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A;
    string B;
    cin >> A >> B;
    long long B100 = (B[0]-'0')*100 + (B[2]-'0')*10 + (B[3]-'0');
    cout << A * B100 / 100 << endl;
}
