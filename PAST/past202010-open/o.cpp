#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<long long> A(N);
    mcf_graph<int, long long> g(N+1);
    long long X=0;
    for (int i=0;i<N;i++) {
        cin>>A[i];
        X+=A[i];
        g.add_edge(i, i+1, 1, A[i]);
        g.add_edge(i+1, i, 1, 0);
    }
    for (int i=0;i<M;i++) {
        int l,r;
        long long c;
        cin >> l >> r >> c;
        g.add_edge(l-1, r, 1, c);
    }
    auto [_, cost] = g.flow(0, N, 1);
    cout << X-cost << endl;
}
