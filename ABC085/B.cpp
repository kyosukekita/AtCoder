#include <bits/stdc++.h>
using namespace std;

  
int main() {
  int N;
  cin >> N;
  
  set<int> d;
  for(int i=0; i<N; i++){
    int k;
    cin >> k;
    d.insert(k);
  }
  
  
  cout << d.size()  << endl;
}
