#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,Q;
    cin >> N >> Q;
    dsu uf(N);
    vector<set<int>> G(N);
    for (int i=0;i<Q;i++) {
        int t;
        cin >> t;
        if (t==1) {
            int u,v;
            cin >> u >> v;
            u--;v--;
            if (!uf.same(u,v)) {
                uf.merge(u,v);
                G[u].insert(v);
                G[v].insert(u);
            }
        } else {
            int u;
            cin >> u;
            u--;
            set<int> s;
            queue<int> q;
            q.push(u);
            s.insert(u);
            while (!q.empty()) {
                int v = q.front();
                q.pop();
                for (int w:G[v]) {
                    if (!s.contains(w)) {
                        s.insert(w);
                        q.push(w);
                    }
                }
            }
            int i = 0;
            for (int v:s) {
                if (i>0) cout << " ";
                cout << v+1;
                i++;
            }
            cout << endl;
        }
    }
}
