int main(){
  int N;
  cin >> N;
  
  bool answer =false;
  while(N>0){
    if(N%10 ==9){
      answer=true;
      break;
    }
    N/=10;
  }
  
  if(answer){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }
}
