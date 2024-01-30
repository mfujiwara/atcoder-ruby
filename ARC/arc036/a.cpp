#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    vector<int> t(N);
    int total = 0;
    for (int i=0;i<N;i++) {
        cin>>t[i];
        total += t[i];
        if (i>=3) {
            total -= t[i-3];
        }
        if (i>=2) {
            if (total<K) {
                cout << i+1 << endl;
                return 0;
            }
        }
    }
    cout << -1 << endl;
}
