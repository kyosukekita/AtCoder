#リュカ数を再帰的に求める。メモ化している。フィボナッチ数列でも同じことができるね。

#include <bits/stdc++.h>
using namespace std;


int main(){
    cout << fixed << setprecision(20);
    long long N;
    cin >> N;

    vector<long long> L(87);

    for(int i=0; i<N+1;i++){
    	if (i==0){
    		L[0]=2;
  		}else if (i==1){
    		L[1]=1;
  		}else{
    		L[i]=L[i-1]+L[i-2];
  		}
    }

    cout << L[N] << endl;
    
    return 0;
}
