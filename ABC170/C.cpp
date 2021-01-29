#include <bits/stdc++.h>
using namespace std;
using ll= long long ;
 
int main(){
  int x, N;
  cin >> x >> N;
  
  //配列を準備
  vector<int> vec(110,0);
  for(int i=0; i<N; i++){
    int p;
    cin >> p;
    vec[p]++;
  }
  
  int y=x;
  int z=x;
  
  int ans1, ans2;
  //xを減らして探す
  while(y>=0){
    if(vec[y]==0){
      ans1=y;
      break;   
    }else{
      y--;
    }
  }
  
  while(z<=101){
    if(vec[z]==0){
      ans2=z;
      break;   
    }else{
      z++;
    }
  }
  
  if(abs(ans1-x) > abs(ans2-x)){
    cout << ans2 << endl;
  }else{
    cout << ans1 << endl;
  }
}  
