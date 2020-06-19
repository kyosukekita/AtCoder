//C++
#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N;
  cin >> N;
  
  vector<long long> A(N);
  for(int i=0; i<N; i++){
    cin >> A[i];
  }
  
  vector<long long> D(N);
  for(int i=0; i<N; i++){
    D[i]=(A[i]-(i+1));
  }
  
  //bはDの中央値
  sort(D.begin(), D.end());
  long long median = D[N>>1];
    
  
  
  long long answer=0;
  for(int i=0; i<N; i++){
    answer+= abs(D[i]-median);
  }
  cout << answer << endl;
    
}





#python
N = int(input())
alist = list(map(int, input().split()))
 
blist = []
 
for i in range(N):
    blist.append(alist[i]-i-1)
 
blist.sort()
mid = blist[N//2]
 
print(sum([abs(b-mid) for b in blist]))
