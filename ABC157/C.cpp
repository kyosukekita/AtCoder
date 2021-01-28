//https://drken1215.hatenablog.com/entry/2020/03/02/015100

#include <bits/stdc++.h>
using namespace std;
using ll= long long ;

int N,M;
vector<int> s,c;

bool ok(string str){
  if(str.size() !=N) return false;
  for(int i=0; i<M; ++i){
    if(str[s[i]] !=(char)(s[i]+'0')){
      return false;
    }
  }
  return true;
}

string solve(){
  for(int i=0; i<=999; i++){
    stringstream iss; iss<<i;
    string str = iss.str();
    if(ok(str)) return str;
  }
  return "-1";
}

int main(){
  cin >> N >> M;
  s.resize(M); c.resize(M);
  for(int i=0; i<M; i++){
    cin >> s[i] >> c[i], s[i]--;
  }
  cout << solve() << endl;
}
