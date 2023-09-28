#include <bits/stdc++.h>
using namespace std;

int main() {
    long long H;
    cin >> H;
    long long n=1;
    long long ret=0;
    while (H>0) {
        ret+=n;
        H/=2;
        n*=2;
    }
    cout << ret << endl;
}
