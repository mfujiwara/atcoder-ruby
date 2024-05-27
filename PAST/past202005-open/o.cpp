#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<long long> A = vector<long long>(N);
    vector<long long> B = vector<long long>(N);
    for (int i=0;i<N;i++) {
        cin>>A[i];
    }
    for (int i=0;i<N;i++) {
        cin>>B[i];
    }
    vector<long long> R = vector<long long>(3);
    for (int i=0;i<3;i++) {
        cin>>R[i];
    }
    vector<vector<long long>> points = vector<vector<long long>>(N, vector<long long>(2));
    for (int i=0;i<N;i++) {
        long long v = A[i];
        for (int j=0;j<3;j++) {
            v *= B[i];
            points[i][j] = v;
        }
    }
    mcf_graph<long long, long long> g(N+5);
    for (int i=0;i<3;i++) {
        g.add_edge(N+3, N+i, M, 0);
        for (int j=0;j<N;j++) {
            long long v = points[j][i]%R[i];
            g.add_edge(N+i, j, 1, R[i]-v);
        }
    }
    for (int i=0;i<N;i++) {
        g.add_edge(i, N+4, 1, points[i][0]);
        g.add_edge(i, N+4, 1, points[i][1]-points[i][0]);
        g.add_edge(i, N+4, 1, points[i][2]-points[i][1]);
    }
    auto [flow, cost] = g.flow(N+3, N+4, M*3);
    cost = -cost + (R[0]+R[1]+R[2])*M;
    cout << cost << endl;
}
