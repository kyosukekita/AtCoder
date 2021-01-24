#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<string> S(N);
  vector<int> P(N);
  for (int i = 0; i < N; i++) {
    cin >> S.at(i) >> P.at(i);
  }
  
  vector<tuple<string, int, int>> restaurant(N);
  for(int i=0; i<N; i++){
    restaurant.at(i)=make_tuple(S.at(i), -P.at(i),i+1);
  }
  sort(restaurant.begin(), restaurant.end());
  
  for(auto i:restaurant){
    cout<< get<2>(i)<< endl;
  }
}
