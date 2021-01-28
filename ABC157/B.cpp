#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

int main() {
  vector<vector<int>> A(3,vector<int>(3));
  for(int i=0; i<3;i++){
    for(int j=0; j<3; j++){
      cin >>A.at(i).at(j);
    }
  }
  int N;
  cin >> N;
  
  int b;
  for(int i=0; i<N; i++){
    cin >> b;
    for(int i=0; i<3; i++){
      for(int j=0; j<3; j++){
        if(b==A[i][j]){
          A[i][j]=0;
        }
      }
    }
  }
  
  bool bingo = false;
  //横でビンゴ
  if((A[0][0]==0 && A[0][1]==0 && A[0][2]==0)|| (A[1][0]==0 && A[1][1]==0 && A[1][2]==0) || (A[2][0]==0 && A[2][1]==0 && A[2][2]==0)){
    bingo=true;
  }
    
  //斜めでビンゴ
  if((A[0][0]==0 && A[1][1]==0 &&A[2][2]==0)|| (A[0][2]==0 && A[1][1]==0 && A[2][0]==0)){
    bingo=true;
  }
  
  //縦でビンゴ
  if((A[0][0]==0 && A[1][0]==0 && A[2][0]==0)|| (A[0][1]==0 && A[1][1]==0 && A[2][1]==0) || (A[0][2]==0 && A[1][2]==0 && A[2][2]==0)){
    bingo=true;
  }
  
  if(bingo){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }
}
