#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  
  int A=0;
  int B=0;
  
  vector<int> vec(N);
  
  for(int i=0;i<N;i++){
    cin >> vec[i];
  }
  
  sort(vec.begin(),vec.end());
  reverse(vec.begin(),vec.end());//大きい順に並べ替え
  
  for(int i=0;i<N;i++){
    if(i%2==0){
      A +=vec.at(i);
    }else{
      B +=vec.at(i);
    }
  }
  
  cout << A-B <<endl;
  
}
