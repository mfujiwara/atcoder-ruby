#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<pair<long,long>> S;
    vector<pair<long,long>> Sx;
    vector<pair<long,long>> Sy;
    for (int i=0;i<N;i++) {
        long x,y;
        cin >> x >> y;
        S.push_back(make_pair(x,y));
        Sx.push_back(make_pair(x,-y));
        Sy.push_back(make_pair(-x,y));
    }
    sort(S.begin(),S.end());
    sort(Sx.begin(),Sx.end());
    sort(Sy.begin(),Sy.end());
    vector<pair<long,long>> T;
    for (int i=0;i<N;i++) {
        long x,y;
        cin >> x >> y;
        T.push_back(make_pair(x,y));
    }
    sort(T.begin(),T.end());
    pair<long long,long long> d = make_pair(0,0);
    pair<long long,long long> dx = make_pair(0,T[0].second-Sx[0].second);
    pair<long long,long long> dy = make_pair(T[0].first-Sy[0].first,0);
    bool b = true;
    bool bx = true;
    bool by = true;
    for (int i=0;i<N;i++) {
        if (b) {
            if (d.first!=T[i].first-S[i].first || d.second!=T[i].second-S[i].second) b = false;
        }
        if (bx) {
            if (dx.first!=T[i].first-Sx[i].first || dx.second!=T[i].second-Sx[i].second) bx = false;
        }
        if (by) {
            if (dy.first!=T[i].first-Sy[i].first || dy.second!=T[i].second-Sy[i].second) by = false;
        }
    }
    if (b || bx || by) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
