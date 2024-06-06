#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<long long> X(3);
    for (int i=0;i<3;i++) {
        cin >> X[i];
    }
    mcf_graph<int, long long> g(N+6);
    string S;
    cin >> S;
    // ab,ac,ba,bc,ca,cb
    for (int i=0;i<S.size();i++) {
        if (S[i] == 'A') {
            g.add_edge(i,N,1,X[0]);
            g.add_edge(i,N+1,1,X[1]);
            g.add_edge(N+2,i,1,0);
            g.add_edge(N+4,i,1,0);
        } else if (S[i] == 'B') {
            g.add_edge(i,N+2,1,X[0]);
            g.add_edge(i,N+3,1,X[2]);
            g.add_edge(N,i,1,0);
            g.add_edge(N+5,i,1,0);
        } else {
            g.add_edge(i,N+4,1,X[1]);
            g.add_edge(i,N+5,1,X[2]);
            g.add_edge(N+1,i,1,0);
            g.add_edge(N+3,i,1,0);
        }
    }
    for (int i=0;i<M;i++) {
        int a,b;
        long long c;
        cin >> a >> b >> c;
        a--;b--;
        g.add_edge(a,b,1,c);
        g.add_edge(b,a,1,c);
    }
    auto ret = g.flow(0,N-1,1);
    cout << ret.second << endl;    
}
