#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    int ret=0;
    for (int i=0;i<N;i++) {
        int x;
        cin >> x;
        ret += min(x, K-x)*2;
    }
    cout << ret << endl;
}
