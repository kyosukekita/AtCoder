#include <bits/stdc++.h>
using namespace std;
using ll= long long;

bool isPrime (ll n);

int main() {
  ll X;
  cin >> X;
  
  while(isPrime(X)==false){
    X+=1;
  }
  cout << X << endl;
}

bool isPrime(ll n){
  if(n==2) return true;
  for(int i=2; i<=sqrt(n);i++){
    if(n%i==0){
      return false;
    }
  }
  return true;
}
