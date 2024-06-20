#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M,K;
    cin >> N >> M >> K;
    vector<long long> H(N);
    for (int i=0;i<N;i++) {
        cin >> H[i];
    }
    auto rets = vector<int>(N,-1);
    vector<int> targets = vector<int>(K);
    for (int i=0;i<K;i++) {
        cin >> targets[i];
        targets[i]--;
        rets[targets[i]] = 0;
    }
    vector<vector<int>> edges = vector<vector<int>>(N,vector<int>());
    for (int i=0;i<M;i++) {
        int a,b;
        cin >> a >> b;
        a--;b--;
        if (H[a] < H[b]) {
            edges[a].push_back(b);
        } else {
            edges[b].push_back(a);
        }
    }
    while (targets.size() > 0) {
        vector<int> next_targets;
        for (int i=0;i<targets.size();i++) {
            int target = targets[i];
            for (int j=0;j<edges[target].size();j++) {
                int next = edges[target][j];
                if (rets[next] == -1) {
                    rets[next] = rets[target] + 1;
                    next_targets.push_back(next);
                }
            }
        }
        targets = next_targets;
    }
    for (int i=0;i<N;i++) {
        cout << rets[i] << endl;
    }
}
