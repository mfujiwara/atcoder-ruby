#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    vector<vector<pair<int,long long>>> G(N);
    for (int i=0;i<M;i++) {
        int u,v;
        long long t;
        cin >> u >> v >> t;
        u--;
        v--;
        G[u].push_back({v,t});
        G[v].push_back({u,t});
    }
    priority_queue<tuple<long long,long long, int>> pq;
    pq.push({0,A[0],0});
    vector<pair<long long,long long>> dist(N,{LLONG_MAX,0});
    while (!pq.empty()) {
        auto [d,a,u] = pq.top();
        d = -d;
        pq.pop();
        if (dist[u].first < d) {
            continue;
        }
        if (dist[u].first == d && dist[u].second > a) {
            continue;
        }
        dist[u] = {d,a};
        for (auto [v,t]:G[u]) {
            long long nd = d+t;
            long long na = a+A[v];
            if (dist[v].first < nd) {
                continue;
            }
            if (dist[v].first == nd && dist[v].second > na) {
                continue;
            }
            pq.push({-nd,na,v});
        }
    }
    cout << dist[N-1].second << endl;
}
