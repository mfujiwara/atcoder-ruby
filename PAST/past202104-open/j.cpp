#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,C;
    cin >> N >> C;
    vector<double> x(N);
    vector<long long> y(N);
    for (int i=0;i<N;i++) {
        cin >> x[i] >> y[i];
    }
    double ret = 0;
    for (int i=0;i<N;i++) {
        ret += (y[i]-C)*(y[i]-C);
    }
    // sort x
    sort(x.begin(),x.end());
    double left = x[0];
    double right = x[N-1];
    while (right-left > 1e-6) {
        double mid1 = left + (right-left)/3;
        double mid2 = right - (right-left)/3;
        double ret1 = 0;
        double ret2 = 0;
        for (int i=0;i<N;i++) {
            ret1 += (x[i]-mid1)*(x[i]-mid1);
            ret2 += (x[i]-mid2)*(x[i]-mid2);
        }
        if (ret1 < ret2) {
            right = mid2;
        } else if (ret1 > ret2) {
            left = mid1;
        } else {
            left = mid1;
            right = mid2;
        }
    }
    cout << fixed << setprecision(10);
    for (int i=0;i<N;i++) {
        ret += (x[i]-left)*(x[i]-left);
    }
    cout << ret << endl;
}
