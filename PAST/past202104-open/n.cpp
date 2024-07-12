#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,H;
    cin >> N >> H;
    vector<pair<long long,long long>> ab(N);
    for (int i=0;i<N;i++) {
        long long a,b;
        cin >> a >> b;
        ab[i] = make_pair(a,b);
    }
    sort(ab.begin(),ab.end(),[](pair<long long,long long> a,pair<long long,long long> b){
        auto v1 = a.first*b.second;
        auto v2 = a.second*b.first;
        if (v1 == v2) {
            return a.first > b.first;
        } else {
            return v1 > v2;
        }
    });
    vector<bool> flgs(N,false);
    int tmp=0;
    for (int i=N-1;i>=0;i--) {
        if (ab[i].first >= tmp) {
            flgs[i] = true;
            tmp = ab[i].first;
        }
    }
    long long ret = 0;
    map<long long,long long> mp;
    mp[H] = 0;
    for (int i=0;i<N;i++) {
        auto [a,b] = ab[i];
        map<long long,long long> mp2;
        for (auto [k,v]:mp) {
            if (!flgs[i]) {
                if (mp2.find(k) == mp2.end()) {
                    mp2[k] = v;
                } else {
                    mp2[k] = max(mp2[k],v);
                }
            }
            auto v1 = v+k*a;
            ret = max(ret,v1);
            if (k-b>0) {
                if (mp2.find(k-b) == mp2.end()) {
                    mp2[k-b] = v1;
                } else {
                    mp2[k-b] = max(mp2[k-b],v1);
                }
            }
        }
        mp = mp2;
    }
    cout << ret << endl;
}
