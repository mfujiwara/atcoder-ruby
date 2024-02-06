#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A,B,C;
    cin >> A >> B >> C;
    long long total = A+B+C;
    long long ret = 0;
    while (A%2==0 && B%2==0 && C%2==0) {
        if (A==B && B==C) {
            cout << -1 << endl;
            return 0;
        }
        A = (total-A)/2;
        B = (total-B)/2;
        C = (total-C)/2;
        ret++;
    }
    cout << ret << endl;
}
