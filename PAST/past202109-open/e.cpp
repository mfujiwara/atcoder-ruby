#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,K;
    cin >> N >> K;
    vector<long long> C(N);
    for (int i=0;i<N;i++) {
        cin >> C[i];
    }
    vector<long long> P(N);
    for (int i=0;i<N;i++) {
        cin >> P[i];
    }
    map<long long,long long> CP;
    for (int i=0;i<N;i++) {
        if (CP.find(C[i]) == CP.end()) {
            CP[C[i]] = P[i];
        } else {
            CP[C[i]] = min(CP[C[i]],P[i]);
        }
    }
    if (CP.size() < K) {
        cout << -1 << endl;
        return 0;
    }
    vector<pair<long long,long long>> PC;
    for (auto cp : CP) {
        PC.push_back({cp.second,cp.first});
    }
    sort(PC.begin(),PC.end());
    long long ans = 0;
    for (int i=0;i<K;i++) {
        ans += PC[i].first;
    }
    cout << ans << endl;
}
