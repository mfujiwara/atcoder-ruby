#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

long long op(long long a, long long b) { return max(a, b); }
long long e() { return -100000000000000; }

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    vector<long long> sums(N+1);
    for (int i=0;i<N;i++) {
        sums[i+1] = sums[i] + A[i];
    }
    segtree<long long, op, e> seg(sums);
    long long ans = -10000000000;
    for (int i=1;i<=N;i++) {
        long long v = seg.prod(i, N+1) - sums[i-1];
        ans = max(ans, v);
    }
    cout << ans << endl;
}
