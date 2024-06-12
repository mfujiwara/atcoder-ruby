#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<vector<int>> G(N,vector<int>(0));
    map<pair<int,int>,int> edgeToIndex;
    for (int i=0;i<N-1;i++) {
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        G[a].push_back(b);
        G[b].push_back(a);
        edgeToIndex[make_pair(a,b)] = i;
        edgeToIndex[make_pair(b,a)] = i;
    }
    vector<int> parents(N);
    parents[0] = -1;
    vector<set<int>> children(N);
    vector<int> depth(N);
    depth[0] = 0;
    queue<int> q;
    q.push(0);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u:G[v]) {
            if (u == parents[v]) continue;
            parents[u] = v;
            depth[u] = depth[v] + 1;
            children[v].insert(u);
            q.push(u);
        }
    }
    vector<vector<int>> queries(Q);
    for (int i=0;i<Q;i++) {
        int u,v,c;
        cin >> u >> v >> c;
        u--;
        v--;
        queries[i] = {u,v,c};
    }
    vector<int> rets(N-1);
    dsu uf(N);
    vector<int> highest(N);
    for (int i=0;i<N;i++) {
        highest[i] = i;
    }
    for (int i=Q-1;i>=0;i--) {
        int u = queries[i][0];
        int v = queries[i][1];
        int c = queries[i][2];
        u = highest[uf.leader(u)];
        v = highest[uf.leader(v)];
        while (u!=v) {
            int t = depth[u] > depth[v] ? u : v;
            int p = parents[t];
            rets[edgeToIndex[make_pair(t,p)]] = c;
            int pp = highest[uf.leader(p)];
            uf.merge(t,p);
            highest[uf.leader(t)] = pp;
            if (depth[u] > depth[v]) {
                u = highest[uf.leader(u)];
            } else {
                v = highest[uf.leader(v)];
            }
        }
    }
    for (int i=0;i<N-1;i++) {
        cout << rets[i] << endl;
    }
}
