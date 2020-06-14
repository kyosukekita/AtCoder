#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
 
int main() {
  int H,W;
  cin >> H>> W;
  
  vector<vector<char>> data(H+2,vector<char>(W+2,'#'));

  rep(i,H){
    rep(j,W){
      cin>>data.at(i+1).at(j+1);
    }
  }
  
  rep(i,H+2){
    rep(j,W+2){
      if(j == W+1){
        cout << data.at(i).at(j)<< endl;
      }
      else{
        cout << data.at(i).at(j);
      }
    }
  }
  
}
