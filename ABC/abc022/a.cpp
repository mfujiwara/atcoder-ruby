#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,S,T,W;
    cin >> N >> S >> T >> W;
    int ret = 0;
    if (S <= W && W <= T) {
        ret++;
    }
    for (int i=0;i<N-1;i++) {
        int A;
        cin >> A;
        W += A;
        if (S <= W && W <= T) {
            ret++;
        }
    }
    cout << ret << endl;
}
