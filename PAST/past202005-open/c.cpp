#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long A,R,N;
    cin >> A >> R >> N;
    if (R==1) {
        if (A > 1000000000) {
            cout << "large" << endl;
        } else {
            cout << A << endl;
        }
    } else {
        long long ret = A;
        for (int i=1;i<N;i++) {
            ret *= R;
            if (ret > 1000000000) {
                cout << "large" << endl;
                return 0;
            }
        }
        cout << ret << endl;
    }
}
