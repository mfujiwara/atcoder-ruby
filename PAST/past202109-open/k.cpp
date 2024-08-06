#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long P,Q;
    cin >> P >> Q;
    vector<string> S;
    for (int i=0;i<P;i++) {
        string s;
        cin >> s;
        S.push_back(s);
    }
    long long base = 0;
    vector<long long> happyP = vector<long long>(P,0);
    vector<long long> happyQ = vector<long long>(Q,0);
    for (int i=0;i<P;i++) {
        long long a,b;
        cin >> a >> b;
        happyP[i] = a-b;
        base += b;
    }
    for (int i=0;i<Q;i++) {
        long long a,b;
        cin >> a >> b;
        happyQ[i] = a-b;
        base += b;
    }
    mcf_graph<int, long long> g(P+Q+2);
    int source = P+Q;
    int sink = P+Q+1;
    for (int i=0;i<P;i++) {
        g.add_edge(source,i,1,0);
    }
    for (int i=0;i<Q;i++) {
        g.add_edge(P+i,sink,1,0);
    }
    for (int i=0;i<P;i++) {
        for (int j=0;j<Q;j++) {
            if (S[i][j] == '1') {
                g.add_edge(i,P+j,1,2000000000-happyP[i]-happyQ[j]);
            }
        }
    }
    g.add_edge(source,sink,P,2000000000);
    auto [flow, cost] = g.flow(source,sink,P);
    cout << 2000000000*P-cost+base << endl;
}
