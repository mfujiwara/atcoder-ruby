#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    long long MOD = 998244353;
    long long N;
    cin >> N;
    vector<long long> fn = {1, 1};
    vector<long long> inv = {1, 1};
    vector<long long> invfn = {1, 1};
    for (long long i = 2; i <= 2*N; i++) {
        fn.push_back(fn.back() * i % MOD);
        inv.push_back(MOD - inv[MOD % i] * (MOD / i) % MOD);
        invfn.push_back(invfn.back() * inv[i] % MOD);
    }
    vector<long long> inv4 = {1};
    for (long long i = 1; i <= N; i++) {
        inv4.push_back(inv4.back() * inv[4] % MOD);
    }
    long long ret = 0;
    for (long long i=1;i<N;i++) {
        long long v = inv4[i]%MOD;
        v = v*fn[2*i]%MOD;
        v = v*invfn[i]%MOD;
        v = v*invfn[i]%MOD;
        v = v*inv[2]%MOD;
        ret = (ret+v)%MOD;
    }
    cout << ret << endl;
}
