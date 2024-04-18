#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<long long> dp(pow(2,N),pow(10,11));
    dp[0] = 0;
    string S;
    long long C;
    for (int i=0;i<M;i++) {
        cin >> S >> C;
        int bit = 0;
        for (int j=0;j<S.size();j++) {
            bit *= 2;
            bit += (S[j]=='Y'?1:0);
        }
        for (int j=pow(2,N)-1;j>=0;j--) {
            int k = j|bit;
            dp[k] = min(dp[k],dp[j]+C);
        }
    }
    if (dp[pow(2,N)-1] == pow(10,11)) {
        cout << -1 << endl;
    } else {
        cout << dp[pow(2,N)-1] << endl;
    }
}
