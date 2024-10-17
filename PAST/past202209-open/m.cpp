#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,M;
    cin >> N >> M;
    mcf_graph<int, long long> g(N+1);
    for (int i=0;i<N;i++) {
        g.add_edge(i+1, i, 1, 0);
    }
    for (int i=0;i<N;i++) {
        long long a;
        cin >> a;
        g.add_edge(i, i+1, 1, a);
    }
    for (int i=0;i<M;i++) {
        long long b;
        int l,r;
        cin >> b >> l >> r;
        g.add_edge(l-1, r, 1, b);
    }
    auto ret = g.flow(0, N, 1);
    cout << ret.second << endl;
}
