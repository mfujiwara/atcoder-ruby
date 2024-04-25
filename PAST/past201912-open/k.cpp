#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

struct Edge {
    long long to;
};
using Graph = vector<vector<Edge>>;

struct LCA {
    vector<vector<int>> parent;  // parent[k][u]:= u の 2^k 先の親
    vector<int> dist;            // root からの距離
    LCA(const Graph &G, int root = 0) { init(G, root); }

    void init(const Graph &G, int root = 0) {
        int V = G.size();
        int K = 1;
        while ((1 << K) < V) K++;
        parent.assign(K, vector<int>(V, -1));
        dist.assign(V, -1);
        dfs(G, root, -1, 0);
        for (int k = 0; k + 1 < K; k++) {
            for (int v = 0; v < V; v++) {
                if (parent[k][v] < 0) {
                    parent[k + 1][v] = -1;
                } else {
                    parent[k + 1][v] = parent[k][parent[k][v]];
                }
            }
        }
    }

    void dfs(const Graph &G, int v, int p, int d) {
        parent[0][v] = p;
        dist[v] = d;
        for (auto e : G[v]) {
            if (e.to != p) dfs(G, e.to, v, d + 1);
        }
    }

    int query(int u, int v) {
        if (dist[u] < dist[v]) swap(u, v);  // u の方が深いとする
        int K = parent.size();
        // LCA までの距離を同じにする
        for (int k = 0; k < K; k++) {
            if ((dist[u] - dist[v]) >> k & 1) {
                u = parent[k][u];
            }
        }
        // 二分探索で LCA を求める
        if (u == v) return u;
        for (int k = K - 1; k >= 0; k--) {
            if (parent[k][u] != parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        }
        return parent[0][u];
    }
};

int main() {
    int N;
    cin >> N;
    Graph G(N);
    int root = -1;
    for (int i=0; i<N; i++) {
        int p;
        cin >> p;
        p--;
        if (p>=0) {
            G[p].push_back({i});
        } else {
            root = i;
        }
    }
    LCA lca(G, root);
    int Q;
    cin >> Q;
    for (int i=0; i<Q; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        int t = lca.query(u, v);
        if (t==v) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
}
