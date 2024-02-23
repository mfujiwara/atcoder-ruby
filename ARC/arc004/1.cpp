#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> xy(N);
    int x,y;
    for (int i=0;i<N;i++) {
        cin >> x >> y;
        xy[i] = make_pair(x,y);
    }
    double max = 0;
    for (int i=0;i<N;i++) {
        for (int j=0;j<N;j++) {
            if (i==j) continue;
            double d = pow(xy[i].first-xy[j].first,2)+pow(xy[i].second-xy[j].second,2);
            if (d>max) max = d;
        }
    }
    cout << fixed << setprecision(10);
    cout << sqrt(max) << endl;
}
