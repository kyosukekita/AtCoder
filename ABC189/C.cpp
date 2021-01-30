#include<bits/stdc++.h>
using namespace std;

int a[10010];
int main(){
	int n;
	cin >> n;
	for(int i=0;i<n;i++)cin >> a[i];

	int ans=0;
	for(int l=0;l<n;l++){
		int x=a[l];
		for(int r=l;r<n;r++){
			x=min(x,a[r]);
			ans=max(ans,x*(r-l+1));
		}
	}
	cout << ans;
}


//WA
#include<bits/stdc++.h>
using namespace std;
using ll= long long;
int main(){
  ll N;
  cin >> N;
  
  vector<ll> vec(N);
  for(int i=0; i<N; i++){
    cin >> vec[i];
  }
  
  int l=0;
  int r=N;
  ll sum=-1;
  while(l<=r && l<N && r-1>=0){
    ll x;
    x=*min_element(vec.begin()+l,vec.begin()+r);
    if(sum < (r-l)*x){
      sum = (r-l)*x;
    }else{
      if(vec[r-1]>=vec[l]){
        l++;
      }else{
        r--;
      }
    }
  }
  cout << sum << endl;
}
