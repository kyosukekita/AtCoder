#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  
  vector<int> a(N);
  for(int i=0; i<N; i++){
    cin >> a.at(i);
  }
  
  int maximum=*max_element(a.begin(),a.end());
  int minimum=*min_element(a.begin(),a.end());
  
  cout << maximum-minimum << endl;
  
  
}
