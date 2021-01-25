#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  ll N;
  cin >> N;

  vector<ll> A(N);
  rep(i,N){
    cin >> A.at(i);
  }
  
  ll max= *std::max_element(A.begin(),A.end());
  
  vector<ll> B(max+2,0);
  rep(i,N){
    B.at(A.at(i))+=1;
    B.at(A.at(i)+1)+=1;
    if (A.at(i)>1)B.at(A.at(i)-1)+=1; 
  }
  
  ll answer= *std::max_element(B.begin(),B.end());
  
  cout<< answer <<endl;
}


//1つだけREになってしまう回答。どこがまずいかわからない...
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0;i<n; i++)
#define all(v) v.begin(), v.end()
using ll = long long;

int main(){
  int N;
  cin >> N;

  vector<int> A(N);
  rep(i,N){
    cin >> A.at(i);
  }
  
  int max= *std::max_element(A.begin(),A.end());
  
  vector<int> B(max+1,0);
  rep(i,N){
    B.at(A.at(i))+=1;
  }
  
  int answer=0;
  if (N>=3){
    for(auto iter= B.begin(); iter !=B.end()-2; iter++){
      int tmp= (*iter)+*(iter+1)+*(iter+2);
      if(tmp>answer){
        answer=tmp;
      }
    }
  }else if (N==2){
    if(B.size()>3){
      answer=1;
    }else{
      answer=2;
    }
  }else if (N==1){
    answer=1;
  }
  cout<< answer <<endl;
}

