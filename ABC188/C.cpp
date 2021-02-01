#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

int main(){
  int N;
  cin >> N;
  
  vector<ll> A(pow(2,N));
  for(int i=0; i<pow(2,N); i++){
    cin >> A.at(i);
  }
  
  vector<ll> B;
  for(int i=0; i<pow(2,N-1);i++){
    B.push_back(A[i]);
  }
  
  vector<ll> C;
  for(int i=pow(2,N-1); i<pow(2,N);i++){
    C.push_back(A[i]);
  }
  
  auto maxB= *std::max_element(B.begin(),B.end());
  auto maxC= *std::max_element(C.begin(),C.end());

  
  ll wanted=min(maxB, maxC);
  auto itr=std::find(A.begin(),A.end(), wanted);
  const ll wanted_index=std::distance(A.begin(), itr);
  cout << wanted_index+1 << endl;
}
  
