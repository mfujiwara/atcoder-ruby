#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    for (int i=0;i<M;i++) {
        int A;
        cin >> A;
        N -= A;
    }
    if (N>=0) {
        cout << N << endl;
    } else {
        cout << -1 << endl;
    }
}
