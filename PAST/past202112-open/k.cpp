#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M,Q,K;
    cin >> N >> M >> Q >> K;
    vector<int> A;
    for (int i=0;i<K;i++) {
        int a;
        cin >> a;
        a--;
        A.push_back(a);
    }
    vector<set<int>> G(N,set<int>());
    for (int i=0;i<M;i++) {
        int u,v;
        cin >> u >> v;
        u--; v--;
        G[u].insert(v);
        G[v].insert(u);
    }
    vector<vector<int>> dists = vector<vector<int>>(K,vector<int>(N,-1));
    for (int i=0;i<K;i++) {
        queue<int> q;
        q.push(A[i]);
        dists[i][A[i]] = 0;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int u:G[v]) {
                if (dists[i][u] == -1) {
                    dists[i][u] = dists[i][v] + 1;
                    q.push(u);
                }
            }
        }
    }
    for (int i=0;i<Q;i++) {
        int s,t;
        cin >> s >> t;
        s--; t--;
        int ans = 1e9;
        for (int j=0;j<K;j++) {
            ans = min(ans,dists[j][s]+dists[j][t]);
        }
        cout << ans << endl;
    }
}
