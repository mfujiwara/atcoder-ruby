#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    long long X;
    cin >> N >> X;
    vector<vector<pair<int,long long>>> G(N,vector<pair<int,long long>>(0));
    for (int i=0;i<N-1;i++) {
        int u,v;
        long long w;
        cin >> u >> v >> w;
        u--;
        v--;
        G[u].push_back(make_pair(v,w));
        G[v].push_back(make_pair(u,w));
    }
    for (int i=0;i<N;i++) {
        vector<long long> dist(N,-1);
        queue<int> q;
        q.push(i);
        dist[i] = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto [v,w]:G[u]) {
                if (dist[v] != -1) {
                    continue;
                }
                dist[v] = dist[u] + w;
                if (dist[v] == X) {
                    cout << "Yes" << endl;
                    return 0;
                }
                if (dist[v] < X) {
                    q.push(v);
                }
            }
        }
    }
    cout << "No" << endl;
}
