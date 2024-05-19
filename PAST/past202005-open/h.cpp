#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,L;
    cin >> N >> L;
    set<int> X;
    for (int i=0;i<N;i++) {
        int x;
        cin >> x;
        X.insert(x);
    }
    int T1,T2,T3;
    cin >> T1 >> T2 >> T3;
    vector<int> dp(L+1, 1e9);
    dp[0] = 0;
    for (int i=1;i<=L;i++) {
        dp[i] = min(dp[i], dp[i-1]+T1);
        if (i>=2) {
            dp[i] = min(dp[i], dp[i-2]+T1+T2);
        }
        if (i>=4) {
            dp[i] = min(dp[i], dp[i-4]+T1+3*T2);
        }
        if (X.count(i)) {
            dp[i] += T3;
        }
    }
    int ret = dp[L];
    ret = min(ret, dp[L-1]+T1/2+T2/2);
    ret = min(ret, dp[L-2]+T1/2+T2/2+T2);
    if (L>=3) {
        ret = min(ret, dp[L-3]+T1/2+T2/2+2*T2);
    }
    cout << ret << endl;
}
