#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,M;
    cin >> N >> M;
    vector<set<int>> G(N);
    for (int i=0;i<M;i++) {
        int A,B;
        cin >> A >> B;
        A--;
        B--;
        G[A].insert(B);
    }
    for (int i=0;i<N;i++) {
        vector<bool> visited(N, false);
        queue<int> q;
        q.push(i);
        for (int j=0;j<M;j++) {
            if (q.empty()) break;
            int v = q.front();
            q.pop();
            for (int u: G[v]) {
                if (u == i) {
                    cout << "No" << endl;
                    return 0;
                }
                if (visited[u]) continue;
                visited[u] = true;
                q.push(u);
            }
        }
    }
    cout << "Yes" << endl;
}
