#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    vector<int> h(N);
    for (int i=0;i<N;i++) {
        cin >> h[i];
    }
    sort(h.begin(), h.end());
    int ret = 1000000000;
    for (int i=0;i<N-K+1;i++) {
        ret = min(ret, h[i+K-1]-h[i]);
    }
    cout << ret << endl;
}
