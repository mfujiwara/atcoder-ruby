#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<vector<int>> G(N, vector<int>());
    for (int i=0;i<M;i++) {
        int u,v;
        cin >> u >> v;
        u--;v--;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    int s,K;
    cin >> s >> K;
    s--;
    vector<int> T(K);
    map<int, int> k_index;
    for (int i=0;i<K;i++) {
        cin >> T[i];
        T[i]--;
        k_index[T[i]] = i;
    }
    vector<vector<int>> dist(K, vector<int>(K, 1e9));
    for (int i=0;i<K;i++) {
        vector<int> d(N, 1e9);
        d[T[i]] = 0;
        queue<int> q;
        q.push(T[i]);
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int u : G[v]) {
                if (d[u] > d[v] + 1) {
                    d[u] = d[v] + 1;
                    q.push(u);
                }
            }
        }
        for (int j=0;j<K;j++) {
            dist[i][j] = d[T[j]];
        }
    }
    vector<int> s_dist(N, 1e9);
    s_dist[s] = 0;
    queue<int> q;
    q.push(s);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : G[v]) {
            if (s_dist[u] > s_dist[v] + 1) {
                s_dist[u] = s_dist[v] + 1;
                q.push(u);
            }
        }
    }
    vector<vector<int>> dp(1<<K, vector<int>(K, 1e9));
    for (int i=0;i<K;i++) {
        dp[1<<i][i] = s_dist[T[i]];
    }
    for (int bit=0;bit<(1<<K);bit++) {
        for (int i=0;i<K;i++) {
            if (bit & (1<<i)) {
                for (int j=0;j<K;j++) {
                    if (bit & (1<<j)) {
                        dp[bit][i] = min(dp[bit][i], dp[bit^(1<<i)][j] + dist[j][i]);
                    }
                }
            }
        }
    }
    int ans = 1e9;
    for (int i=0;i<K;i++) {
        ans = min(ans, dp[(1<<K)-1][i]);
    }
    cout << ans << endl;
}
