#include <bits/stdc++.h>

using namespace std;

int main() {
    long long A,B;
    cin >> A >> B;
    long long g=gcd(A,B);
    cout << A*B/g <<endl;
}

long long gcd(int a, int b){
  if(a%b == 0){
    return b;
  }else{
    return gcd(b, a%b);
  }
}
