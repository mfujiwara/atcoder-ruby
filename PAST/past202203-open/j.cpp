#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    long long MOD = 998244353;
    int N,K;
    cin >> N >> K;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    sort(A.begin(),A.end());
    vector<long long> kaijou(N+1,1);
    vector<long long> inv(N+1,1);
    vector<long long> kaijou_inv(N+1,1);
    for (long long i=2;i<=N;i++) {
        kaijou[i] = kaijou[i-1]*i%MOD;
        inv[i] = MOD - inv[MOD%i]*(MOD/i)%MOD;
        kaijou_inv[i] = kaijou_inv[i-1]*inv[i]%MOD;
    }
    long long ret = 0;
    for (int i=0;i<N-K+1;i++) {
        long long r = (A[N-1-i] - A[i]+MOD)%MOD;
        r = r*kaijou[N-1-i]%MOD;
        r = r*kaijou_inv[K-1]%MOD;
        r = r*kaijou_inv[N-K-i]%MOD;
        ret = (ret+r)%MOD;
    }
    ret = ret*kaijou_inv[N]%MOD;
    ret = ret*kaijou[K]%MOD;
    ret = ret*kaijou[N-K]%MOD;
    ret = (ret+MOD)%MOD;
    cout << ret << endl;
}
