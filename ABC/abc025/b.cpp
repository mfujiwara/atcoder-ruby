#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,A,B;
    cin >> N >> A >> B;
    string s;
    int d;
    int ret = 0;
    for (int i=0;i<N;i++) {
        cin >> s >> d;
        if (s == "East") {
            if (d < A) {
                d = A;
            } else if (d > B) {
                d = B;
            }
            ret += d;
        } else {
            if (d < A) {
                d = A;
            } else if (d > B) {
                d = B;
            }
            ret -= d;
        }
    }
    if (ret == 0) {
        cout << 0 << endl;
    } else if (ret > 0) {
        cout << "East " << ret << endl;
    } else {
        cout << "West " << -ret << endl;
    }
}
