#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,K;
    cin >> A >> B >> K;
    for (int i=0;i<K;i++) {
        if (i%2==0) {
            if (A%2==1) {
                A-=1;
            }
            A/=2;
            B+=A;
        } else {
            if (B%2==1) {
                B-=1;
            }
            B/=2;
            A+=B;
        }
    }
    cout << A << " " << B << endl;
}
