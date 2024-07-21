#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<set<int>> edges(N);
    vector<set<int>> parents(N);
    for (int i=0;i<M;i++) {
        int u,v;
        cin >> u >> v;
        u--;v--;
        edges[u].insert(v);
        parents[v].insert(u);
    }
    queue<int> q;
    for (int i=0;i<N;i++) {
        if (edges[i].size() == 0) {
            q.push(i);
        }
    }
    while(!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v:parents[u]) {
            edges[v].erase(u);
            if (edges[v].size() == 0) {
                q.push(v);
            }
        }
    }
    for (int i=0;i<N;i++) {
        if (edges[i].size() > 0) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
}
