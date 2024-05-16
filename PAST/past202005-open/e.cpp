#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M,Q;
    cin >> N >> M >> Q;
    vector<vector<int>> G(N,vector<int>());
    for (int i=0;i<M;i++) {
        int u,v;
        cin >> u >> v;
        u-=1;
        v-=1;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    vector<int> C(N);
    for (int i=0;i<N;i++) {
        cin >> C[i];        
    }
    for (int i=0;i<Q;i++) {
        int s;
        cin >> s;
        if (s == 1) {
            int x;
            cin >> x;
            x-=1;
            cout << C[x] << endl;
            for (int j=0;j<G[x].size();j++) {
                C[G[x][j]] = C[x];
            }
        } else {
            int x,y;
            cin >> x >> y;
            x-=1;
            cout << C[x] << endl;
            C[x] = y;
        }
    }
}
