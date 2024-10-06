#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

pair<vector<long long>, vector<long long>> dijkstra(vector<vector<pair<int,long long>>> &G, int s) {
    int n = G.size();
    vector<long long> dist(n, LLONG_MAX);
    vector<long long> prev(n, -1);
    dist[s] = 0;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> que;
    que.push({0,s});
    while (!que.empty()) {
        auto [d,v] = que.top();
        d = -d;
        que.pop();
        if (dist[v] < d) continue;
        for (auto [to,cost]:G[v]) {
            if (dist[to] > dist[v]+cost) {
                dist[to] = dist[v]+cost;
                prev[to] = v;
                que.push({dist[to],to});
            }
        }
    }
    return {dist,prev};
}

int main() {
    int H,W;
    cin >> H >> W;
    vector<vector<long long>> C(H, vector<long long>(W));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cin >> C[i][j];
        }
    }
    C[0][0] = 100000000000;
    C[H-1][W-1] = 100000000000;
    int s = H*W;
    int t = H*W+1;
    vector<vector<pair<int,long long>>> g(H*W+2);
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            if (j<W-1) {
                g[i*W+j].push_back({i*W+j+1,C[i][j+1]});
                g[i*W+j+1].push_back({i*W+j,C[i][j]});
            }
            if (i>0) {
                g[i*W+j].push_back({(i-1)*W+j,C[i-1][j]});
                g[(i-1)*W+j].push_back({i*W+j,C[i][j]});
            }
            if (j<W-1 && i>0) {
                g[i*W+j].push_back({(i-1)*W+j+1,C[i-1][j+1]});
                g[(i-1)*W+j+1].push_back({i*W+j,C[i][j]});
            }
            if (j>0 && i>0) {
                g[i*W+j].push_back({(i-1)*W+j-1,C[i-1][j-1]});
                g[(i-1)*W+j-1].push_back({i*W+j,C[i][j]});
            }
            if (j==0 || i==H-1) {
                g[s].push_back({i*W+j,C[i][j]});
            }
            if (j==W-1 || i==0) {
                g[i*W+j].push_back({t,0});
            }
        }
    }
    auto [dist,prev] = dijkstra(g,s);
    cout << dist[t] << endl;
    set<int> walls;
    int now = t;
    while (now != s) {
        int prevv = prev[now];
        walls.insert(prevv);
        now = prevv;
    }
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            if (walls.count(i*W+j)) {
                cout << "#";
            } else {
                cout << ".";
            }
        }
        cout << endl;
    }
}
