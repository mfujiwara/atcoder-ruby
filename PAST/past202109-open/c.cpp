#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    long long X;
    cin >> N >> X;
    int ret = 0;
    for (int i=0;i<N;i++) {
        long long A;
        cin >> A;
        if (A==X) {
            ret++;
        }
    }
    cout << ret << endl;
}
