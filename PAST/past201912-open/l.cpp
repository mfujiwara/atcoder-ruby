#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<vector<int>> A(N);
    for (int i=0;i<N;i++) {
        int x,y,c;
        cin >> x >> y >> c;
        A[i] = {x,y,c};
    }
    vector<vector<int>> B(M);
    for (int i=0;i<M;i++) {
        int x,y,c;
        cin >> x >> y >> c;
        B[i] = {x,y,c};
    }
    double ret = pow(10,9);
    for (int i=0;i<pow(2,M);i++) {
        vector<vector<int>> C = A;
        for (int j=0;j<M;j++) {
            if (i>>j&1) {
                C.push_back(B[j]);
            }
        }
        vector<vector<double>> edges;
        for (int j=0;j<C.size();j++) {
            for (int k=j+1;k<C.size();k++) {
                int x1 = C[j][0];
                int y1 = C[j][1];
                int c1 = C[j][2];
                int x2 = C[k][0];
                int y2 = C[k][1];
                int c2 = C[k][2];
                double d = sqrt(pow(x1-x2,2)+pow(y1-y2,2));
                if (c1!=c2) {
                    d = d*10;
                }
                edges.push_back({d,j,k});
            }
        }
        sort(edges.begin(),edges.end());
        dsu uf(C.size());
        double cost = 0;
        for (int j=0;j<edges.size();j++) {
            double d = edges[j][0];
            int x = edges[j][1];
            int y = edges[j][2];
            if (!uf.same(x,y)) {
                uf.merge(x,y);
                cost += d;
            }
        }
        ret = min(ret,cost);
    }
    cout << fixed << setprecision(10);
    cout << ret << endl;
}
