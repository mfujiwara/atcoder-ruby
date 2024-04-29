#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<vector<long long>> A(N);
    vector<vector<long long>> vij;
    for (int i=0;i<N;i++) {
        vector<long long> a(6);
        for (int j=0;j<6;j++) {
            cin >> a[j];
        }
        sort(a.begin(), a.end());
        A[i] = a;
        for (int j=0;j<6;j++) {
            vij.push_back({a[j],i,j});
        }
    }
    sort(vij.begin(), vij.end());
    vector<vector<double>> rate(N, vector<double>(6));
    double t = 1.0;
    for (int i=6*N-1;i>=0;i--) {
        long long vi = vij[i][1];
        long long vj = vij[i][2];
        rate[vi][vj] = t;
        double tmp = 1.0;
        for (int j=vj;j<6;j++) {
            tmp += rate[vi][j]/6.0;
        }
        if (tmp > t) {
            t = tmp;
        }
    }
    double ret = 0;
    for (int i=0;i<N;i++) {
        double r = 0;
        for (int j=0;j<6;j++) {
            r += rate[i][j];
        }
        r /= 6.0;
        r += 1;
        ret = max(ret, r);
    }
    cout << fixed << setprecision(10);
    cout << ret << endl;
}
