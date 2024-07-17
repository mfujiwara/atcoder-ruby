#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<tuple<int,int,int>> v;
    for (int i=0;i<N;i++) {
        int d,s,t;
        cin >> d >> s >> t;
        v.push_back(make_tuple(d,s,t));
    }
    sort(v.begin(),v.end());
    for (int i=0;i<N-1;i++) {
        auto [d,s,t]=v[i];
        auto [d0,s0,t0]=v[i+1];
        if (d0==d) {
            if (s0<t) {
                cout << "Yes" << endl;
                return 0;
            }
        }
    }
    cout << "No" << endl;
}
