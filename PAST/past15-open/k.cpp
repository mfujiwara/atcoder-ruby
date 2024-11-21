#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

pair<long long,long long> op(pair<long long,long long> a, pair<long long,long long> b) {
    auto [a1, a2] = a;
    auto [b1, b2] = b;
    return {a1+b1, a2+b2};
}
pair<long long,long long> e() { return {0,0}; }

int main() {
    long long N;
    cin >> N;
    vector<pair<long long,long long>> A(N);
    map<long long,long long> mp;
    for (long long i=0;i<N;i++) {
        long long a;
        cin >> a;
        A[i] = {a,1};
        mp[a] = i;
    }
    long long ret = 0;
    segtree<pair<long long,long long>, op, e> seg(A);
    for (long long i=N;i>0;i--) {
        auto [a,b] = seg.prod(mp[i]+1,N);
        ret += a + b*i;
        seg.set(mp[i],{0,0});
    }
    cout << ret << endl;
}
