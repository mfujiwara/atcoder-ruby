#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<double> PX(N);
    vector<double> PY(N);
    for (int i=0;i<N;i++) {
        cin >> PX[i] >> PY[i];
    }
    vector<double> CX(M);
    vector<double> CY(M);
    vector<double> R(M);
    for (int i=0;i<M;i++) {
        cin >> CX[i] >> CY[i] >> R[i];
    }
    vector<vector<double>> dist(N+M,vector<double>(N+M));
    for (int i=0;i<N+M-1;i++) {
        for (int j=i+1;j<N+M;j++) {
            if (i<N && j<N) {
                double d = sqrt((PX[i]-PX[j])*(PX[i]-PX[j])+(PY[i]-PY[j])*(PY[i]-PY[j]));
                dist[i][j] = d;
            } else if (i<N && j>=N) {
                double d = sqrt((PX[i]-CX[j-N])*(PX[i]-CX[j-N])+(PY[i]-CY[j-N])*(PY[i]-CY[j-N]));
                dist[i][j] = abs(d-R[j-N]);
            } else {
                double d = sqrt((CX[i-N]-CX[j-N])*(CX[i-N]-CX[j-N])+(CY[i-N]-CY[j-N])*(CY[i-N]-CY[j-N]));
                if (d >= R[i-N]+R[j-N]) {
                    dist[i][j] = d-R[i-N]-R[j-N];
                } else if (d <= abs(R[i-N]-R[j-N])) {
                    dist[i][j] = abs(R[i-N]-R[j-N])-d;
                } else {
                    dist[i][j] = 0;
                }
            }
        }
    }
    double ret = 1e9;
    for (int bit=0;bit<(1<<M);bit++) {
        vector<int> order;
        for (int i=0;i<N;i++) {
            order.push_back(i);
        }
        for (int j=0;j<M;j++) {
            if (bit&(1<<j)) {
                order.push_back(N+j);
            }
        }
        vector<tuple<double,int,int>> paths;
        for (int i=0;i<(int)order.size()-1;i++) {
            for (int j=i+1;j<(int)order.size();j++) {
                paths.push_back({dist[order[i]][order[j]],order[i],order[j]});
            }
        }
        sort(paths.begin(),paths.end());
        dsu uf(N+M);
        double cost = 0;
        for (auto [d,a,b]:paths) {
            if (uf.same(a,b)) {
                continue;
            }
            uf.merge(a,b);
            cost += d;
        }
        ret = min(ret,cost);
    }
    cout << fixed << setprecision(10);
    cout << ret << endl;
}
