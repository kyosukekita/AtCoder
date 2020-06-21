#include <bits/stdc++.h>
using namespace std;

int main(){
  int A,B;
  cin >> A>>B;
  
  int N;// A,Bをstringで受け取って、stoi(A+B)でＮを求めてもよかった。
  if(B<9){N=10*A+B;}
  if(B>9 && B<100){N=100*A+B;}
  if(B==100){N=1000*A+B;}
  
  bool flag=false;
  for(int i=0; i*i<=N;i++){
    if(i*i==N){
      flag=true;
    }
  }
  
  if(flag==true){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }
}
