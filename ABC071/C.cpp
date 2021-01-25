#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  int N;
  cin >> N;
  
  map<int,int, greater<int>> stick;
  ll A;
  
  rep(i,N){
    cin >> A;
    if(stick.count(A)){
      stick[A]+=1;
    }else{
      stick[A]=1;
    }
  }
  
  ll count=0;
  ll a=0;
  ll b=0;
  for(auto iter=stick.begin(); iter !=stick.end(); iter++){
    if ((iter->second) >=4){
      if(count==0){
        a=(iter->first);
        b=(iter->first);
        break;
      }else if (count==1){
        b= (iter->first);
        break;
      }
 
    }else if ((iter->second) >=2){
      if(count==0){
        a= (iter->first);
        count++;
        continue;
      }else if (count==1){
        b= (iter->first);
        break;
      }
    }else{
      continue;
    }
  }
  
  cout<< a* b << endl;
  
}
  
    
