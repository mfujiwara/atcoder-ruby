#include <bits/stdc++.h>
using namespace std;

int main() {
    int L,H,N;
    cin >> L >> H >> N;
    int A;
    for (int i=0;i<N;i++) {
        cin>>A;
        if (A<L) {
            cout << L-A << endl;
        } else if (A>H) {
            cout << -1 << endl;
        } else {
            cout << 0 << endl;
        }
    }
}
