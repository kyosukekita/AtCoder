#include <bits/stdc++.h>
using namespace std;

int digitSum(int k){
    int sum=0;
    
    while(k>0){
      sum+= (k%10);
      k /=10;
    }
    return sum;
}
  
  
int main() {
  int N;
  cin >> N;
  
  if (N%digitSum(N)==0){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }
  
}
