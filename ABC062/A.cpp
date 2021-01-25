#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  int x,y;
  cin >> x >> y;
  
  vector<int> vec(13);
  rep(i,13){
    if(i==2){
      vec.at(i)=0;
    }else if (i==4 || i==6 || i==9 || i==11){
      vec.at(i)=1;
    }else{
      vec.at(i)=2;
    }
  }
  
  if(vec.at(x)==vec.at(y)){
    cout << "Yes" << endl;
  }else{
    cout <<"No" << endl;
  }
  
}
