#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long INF = 2e18;
    int N,M;
    cin >> N >> M;
    vector<vector<pair<int,long long>>> G(N);
    vector<vector<pair<int,long long>>> invG(N);
    for (int i=0;i<M;i++) {
        int u,v;
        long long w;
        cin >> u >> v >> w;
        u--;v--;
        G[u].push_back({v,w});
        invG[v].push_back({u,w});
    }
    vector<long long> dist(N,INF);
    dist[0] = 0;
    priority_queue<pair<long long,int>> pq;
    pq.emplace(0,0);
    while (pq.empty() == false) {
        auto [d,u] = pq.top();
        d = -d;
        pq.pop();
        if (d != dist[u]) continue;
        for (auto [v,w]:G[u]) {
            long long dd = dist[u]+w;
            if (dist[v] > dd) {
                dist[v] = dd;
                pq.emplace(-dist[v],v);
            }
        }
    }
    vector<long long> invdist(N,INF);
    invdist[N-1] = 0;
    pq.emplace(0,N-1);
    while (pq.empty() == false) {
        auto [d,u] = pq.top();
        d = -d;
        pq.pop();
        if (d != invdist[u]) continue;
        for (auto [v,w]:invG[u]) {
            long long dd = invdist[u]+w;
            if (invdist[v] > dd) {
                invdist[v] = dd;
                pq.emplace(-invdist[v],v);
            }
        }
    }
    for (int i=0;i<N;i++) {
        long long d = dist[i]+invdist[i];
        if (d >= INF) cout << -1 << endl;
        else cout << d << endl;
    }
}
