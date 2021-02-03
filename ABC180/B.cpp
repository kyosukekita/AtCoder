#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  
  vector<int> x(N);
  for(int i=0; i<N;i++){
    cin >> x.at(i);
  }
  
  long long man=0;
  for(int i=0; i<N;i++){
    man+=abs(x[i]);
  }
  cout << man << endl;
  
  long double eu=0;
  for(int i=0; i<N;i++){
    eu+=pow(x[i],2);
  }
  cout << fixed << setprecision(15) << sqrt(eu) << endl;
  
  int che=0;
  for(int i=0; i<N;i++){
    che=max(che,abs(x[i]));
  }
  cout << che << endl;
}
