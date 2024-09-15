#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,A,B;
    cin >> N >> A >> B;
    vector<vector<long long>> dp(A+1, vector<long long>(B+1, 0));
    long long ret = 0;
    for (int i=0;i<N;i++) {
        int w;
        long long v;
        cin >> w >> v;
        for (int a=A;a>=0;a--) {
            for (int b=B;b>=0;b--) {
                if (a-w>=0) {
                    dp[a][b] = max(dp[a][b], dp[a-w][b]+v);
                }
                if (b-w>=0) {
                    dp[a][b] = max(dp[a][b], dp[a][b-w]+v);
                }
                ret = max(ret, dp[a][b]);
            }
        }
    }
    cout << ret << endl;
}
