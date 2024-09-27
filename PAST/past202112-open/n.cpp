#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

double EPS = 1e-10;
double cross(pair<double,double> a, pair<double,double> b) {
    return a.first*b.second-a.second*b.first;
}

int main() {
    int N,M;
    cin >> N >> M;
    vector<pair<double,double>> ab;
    for (int i=0;i<N;i++) {
        double a,b;
        cin >> a >> b;
        ab.push_back(make_pair(a,b));
    }
    vector<pair<double,double>> cd;
    for (int i=0;i<M;i++) {
        double c,d;
        cin >> c >> d;
        cd.push_back(make_pair(c,d));
    }
    for (int i=0;i<M;i++) {
        auto [c0,d0] = cd[i];
        auto [c1,d1] = cd[(i+1)%M];
        auto ccdd = make_pair(c1-c0,d1-d0);
        vector<pair<double,double>> nexts;
        for (int j=0;j<ab.size();j++) {
            auto [a0,b0] = ab[j];
            auto [a1,b1] = ab[(j+1)%ab.size()];
            double v0 = cross(ccdd,make_pair(a0-c0,b0-d0));
            double v1 = cross(ccdd,make_pair(a1-c0,b1-d0));
            if (v0 + EPS > 0) {
                nexts.push_back(ab[j]);
            }
            if ((v0 > EPS && v1 < -EPS) || (v0 < -EPS && v1 > EPS)) {
                nexts.push_back(make_pair(a0-(a1-a0)*v0/(v1-v0),b0-(b1-b0)*v0/(v1-v0)));
            }
        }
        ab = nexts;
    }
    double ret = 0;
    for (int i=0;i<ab.size();i++) {
        ret += cross(ab[i],ab[(i+1)%ab.size()]);
    }
    cout << fixed << setprecision(20) << ret/2 << endl;
}
