#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  
  int A[N];
  for(int i=0; i<N; i++){
    cin >> A[i];
  }
  
  int count =0;
  
  while (true){
    bool exist_odd= false;
    for(int i=0; i<N; i++){
      if (A[i]%2!=0){
        exist_odd=true;
      }
    }
    
    if (exist_odd){
       break;
    }
      
    for(int i=0; i<N; i++){
       A[i] /=2;
    }
    
    count++;
  }
  
  cout << count << endl;
