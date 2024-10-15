#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

long long op(long long a, long long b) { return (a + b)%998244353; }
long long e() { return 0; }

int main() {
    long long MOD = 998244353;
    int Q;
    cin >> Q;
    vector<tuple<string, long long, long long>> queries = {};
    set<pair<long long, long long>> s;
    for (int i=0;i<Q;i++) {
        string t;
        long long x,y;
        cin >> t >> x >> y;
        queries.push_back(make_tuple(t, x, y));
        s.insert(make_pair(x, y));
        s.insert(make_pair(-x, -y));
    }
    vector<pair<long long, long long>> v(s.begin(), s.end());
    sort(v.begin(), v.end(), [](pair<long long, long long> a, pair<long long, long long> b) {
        return atan2l(a.second, a.first) < atan2l(b.second, b.first);
    });
    map<pair<long long, long long>, int> mp;
    for (int i=0;i<v.size();i++) {
        mp[v[i]] = i;
    }
    segtree<long long,op,e> segx(v.size()*2);
    segtree<long long,op,e> segy(v.size()*2);
    long long ret = 0;
    for (int i=0;i<Q;i++) {
        string t;
        long long x,y;
        tie(t, x, y) = queries[i];
        auto it = mp[make_pair(x, y)];
        auto it2 = mp[make_pair(-x, -y)];
        auto it3 = it + v.size();
        if (it > it2) it2 += v.size();

        long long sx,sy;
        if (t == "+") {
            sx = segx.prod(it, it2);
            sy = segy.prod(it, it2);
            ret += ((x*sy) - (y*sx))%MOD;
            ret %= MOD;
            ret = (ret + MOD)%MOD;

            sx = segx.prod(it2, it3);
            sy = segy.prod(it2, it3);
            ret -= ((x*sy) - (y*sx))%MOD;
            ret %= MOD;
            ret = (ret + MOD)%MOD;

            segx.set(it, (segx.get(it) + x)%MOD);
            segx.set(it3, (segx.get(it3) + x)%MOD);
            segy.set(it, (segy.get(it) + y)%MOD);
            segy.set(it3, (segy.get(it3) + y)%MOD);
        } else {
            sx = segx.prod(it, it2);
            sy = segy.prod(it, it2);
            ret -= ((x*sy) - (y*sx))%MOD;
            ret %= MOD;
            ret = (ret + MOD)%MOD;

            sx = segx.prod(it2, it3);
            sy = segy.prod(it2, it3);
            ret += ((x*sy) - (y*sx))%MOD;
            ret %= MOD;
            ret = (ret + MOD)%MOD;

            segx.set(it, (segx.get(it) - x + MOD)%MOD);
            segx.set(it3, (segx.get(it3) - x + MOD)%MOD);
            segy.set(it, (segy.get(it) - y + MOD)%MOD);
            segy.set(it3, (segy.get(it3) - y + MOD)%MOD);
        }
        cout << ret << endl;
    }
}
