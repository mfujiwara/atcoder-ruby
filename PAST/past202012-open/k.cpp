#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int t = 0;
    int bit = 1;
    for (int i=0;i<4;i++) {
        string s;
        cin >> s;
        for (int j=0;j<s.size();j++) {
            if (s[j] == '#') {
                t += bit;
            }
            bit *= 2;
        }
    }
    vector<double> dp(t+1,100);
    dp[0] = 0;
    for (int bit=1;bit<t+1;bit++) {
        for (int j=0;j<16;j++) {
            int cnt = 0;
            double sum = 0;
            if ((bit&(1<<j))==0) {
                cnt += 1;
            } else {
                sum += dp[bit-(1<<j)];
            }
            if (j<4 || (bit&(1<<(j-4)))==0) {
                cnt += 1;
            } else {
                sum += dp[bit-(1<<(j-4))];
            }
            if (j%4==0 || (bit&(1<<(j-1)))==0) {
                cnt += 1;
            } else {
                sum += dp[bit-(1<<(j-1))];
            }
            if (j%4==3 || (bit&(1<<(j+1)))==0) {
                cnt += 1;
            } else {
                sum += dp[bit-(1<<(j+1))];
            }
            if (j>11 || (bit&(1<<(j+4)))==0) {
                cnt += 1;
            } else {
                sum += dp[bit-(1<<(j+4))];
            }
            if (cnt < 5) {
                dp[bit] = min(dp[bit],(sum+5)/(5-cnt));
            }
        }
    }
    cout << fixed << setprecision(10) << dp[t] << endl;
}
