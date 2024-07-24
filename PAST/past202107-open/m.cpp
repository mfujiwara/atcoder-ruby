#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    long long C;
    cin >> N >> C;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    mcf_graph<int, long long> g(2*N+2);
    for (int i=0;i<N-1;i++) {
        for (int j=i+1;j<N;j++) {
            g.add_edge(i,j+N,1,abs(A[i]-A[j]));
        }
    }
    for (int i=0;i<N;i++) {
        g.add_edge(2*N,i,1,0);
        g.add_edge(i+N,2*N+1,1,0);
    }
    g.add_edge(2*N,2*N+1,N,C);
    auto ret = g.flow(2*N,2*N+1,N);
    cout << ret.second << endl;
}
