#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A,B,K;
    cin >> A >> B >> K;
    if (B-A+1<=2*K) {
        for (long long i=A;i<=B;i++) {
            cout << i << endl;
        }
    } else {
        for (long long i=A;i<A+K;i++) {
            cout << i << endl;
        }
        for (long long i=B-K+1;i<=B;i++) {
            cout << i << endl;
        }
    }
}
