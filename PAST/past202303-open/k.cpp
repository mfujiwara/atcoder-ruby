#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,t;
    long double p;
    cin >> N >> t >> p;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    vector<long double> dp(N+2);
    for (int i=N-1;i>=0;i--) {
        long double c0 = A[i]*t/100;
        long double c1 = A[i]-c0;
        long double v1 = c1+dp[i+1];
        long double v2 = (c1+dp[i+2])*p/100 + (A[i]+dp[i+1])*(100-p)/100;
        dp[i] = max(v1,v2);
    }
    cout << fixed << setprecision(10) << dp[0] << endl;
}
