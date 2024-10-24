#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,K;
    cin >> N >> K;
    long long xs,ys,xt,yt;
    cin >> xs >> ys >> xt >> yt;
    vector<long long> cost;
    for (int i=0;i<N;i++) {
        long long p,q,r,w;
        cin >> p >> q >> r >> w;
        long long vs = p*xs+q*ys-r;
        if (vs==0) {
            cost.push_back(w);
            continue;
        }
        long long vt = p*xt+q*yt-r;
        if (vt==0) {
            cost.push_back(w);
            continue;
        }
        if (vs>0 && vt<0 || vs<0 && vt>0) {
            cost.push_back(w);
        } else {
            cost.push_back(0);
        }
    }
    sort(cost.begin(),cost.end());
    long long ret = 0;
    for (int i=0;i<K;i++) {
        ret += cost[i];
    }
    cout << ret << endl;
}
