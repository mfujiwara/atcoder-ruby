#include <bits/stdc++.h>
using namespace std;

int main() {
    unsigned long long A,B,K;
    cin >> A >> B >> K;
    if (A>=K) {
        A-=K;
        K=0;
    } else {
        K-=A;
        A=0;
    }
    if (B>=K) {
        B-=K;
        K=0;
    } else {
        B=0;
    }
    cout << A << " " << B << endl;
}
