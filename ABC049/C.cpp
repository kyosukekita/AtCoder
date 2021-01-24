#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  string S;
  cin >> S;
  string str1 = regex_replace(S, regex("eraser"), ""); //#include <regex>が必要
  string str2 = regex_replace(str1, regex("erase"), "");
  string str3 = regex_replace(str2, regex("dreamer"), "");
  string str4 = regex_replace(str3, regex("dream"), "");
  
  if(str4==""){
    cout<< "YES" << endl;
  }else{
    cout <<"NO" << endl;
  }
}
