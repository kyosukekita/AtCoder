#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  
  vector<int> a(N);
  for(int i=0; i<N; i++){
    cin >> a.at(i);
  }
 
 
  //std::*_element は，イテレーターを返すので '*' で値を取得する.
  //std::vector<int>::iterator
  int maximum=*max_element(a.begin(),a.end());
  int minimum=*min_element(a.begin(),a.end());
  
  cout << maximum-minimum << endl;
  
  
}
